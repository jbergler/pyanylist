"""API Client code"""

from __future__ import annotations

import logging
import os
import uuid

import aiohttp
from multidict import MultiDict

from anylist import messages_pb2 as pb
from anylist.credentials import (
    CREDENTIALS_KEY_ACCESS_TOKEN,
    CREDENTIALS_KEY_CLIENT_ID,
    CREDENTIALS_KEY_REFRESH_TOKEN,
    decrypt_credentials,
    encrypt_credentials,
)
from anylist.shopping_list import ShoppingList
from anylist.shopping_list_item import ShoppingListItem

__all__ = [
    "AnyListClient",
]

# Set up logger
logger = logging.getLogger("anylist.client")


class AnyListClient:
    """Client for interacting with the AnyList API."""

    BASE_URL = "https://www.anylist.com"

    def __init__(self, email, password, credentials_file=None):
        self.email = email
        self.password = password
        self.credentials_file = credentials_file or os.path.expanduser(
            "~/.anylist_credentials"
        )
        self.access_token = None
        self.refresh_token = None
        self.client_id = None
        self.session = None
        self.user_data: pb.PBUserDataResponse | None = None
        self.uid = None

    async def __aenter__(self):
        """Enter the async context manager, creating a session."""
        self.session = aiohttp.ClientSession(
            headers=self._get_auth_headers(auth_required=False),
        )
        return self

    async def __aexit__(self, exc_type, exc, tb):
        """Exit the async context manager, closing the session."""
        await self.session.close()

    async def login(self):
        """Login to AnyList and get access token."""
        await self._load_credentials()
        self.client_id = await self._get_client_id()
        if not self.access_token or not self.refresh_token:
            print("No saved tokens found, fetching new tokens using credentials")
            await self._fetch_tokens()

    async def get_user_data(self, refresh=False) -> pb.PBUserDataResponse:
        """Get all user data from AnyList using the data/user-data/get endpoint.

        This is the primary method to fetch user data from AnyList. It returns a
        dictionary with all user data including lists, items, recipes, etc.
        """
        if self.user_data and not refresh:
            return self.user_data

        self.user_data = await self._request_protobuf(
            "post",
            "data/user-data/get",
            protobuf_response_class=pb.PBUserDataResponse,
        )
        return self.user_data

    async def _fetch_tokens(self):
        """Fetch new access and refresh tokens using email/password."""
        # For token endpoints, we need to use form data instead of JSON
        data = aiohttp.FormData()
        data.add_field("email", self.email)
        data.add_field("password", self.password)

        # Note: We can't use _request here because this is used to get the initial tokens
        # needed for authenticated requests
        url = f"{self.BASE_URL}/auth/token"
        async with self.session.post(url, data=data) as resp:
            resp.raise_for_status()
            result = await resp.json()
            self.access_token = result["access_token"]
            self.refresh_token = result["refresh_token"]
            await self._store_credentials()

    async def _refresh_tokens(self):
        """Refresh access token using refresh token."""
        # For token endpoints, we need to use form data instead of JSON
        data = aiohttp.FormData()
        data.add_field("refresh_token", self.refresh_token)

        try:
            # Note: We can't use _request here because we're handling a token expiration scenario
            # and _request would create a circular dependency
            url = f"{self.BASE_URL}/auth/token/refresh"
            async with self.session.post(url, data=data) as resp:
                resp.raise_for_status()
                result = await resp.json()
                self.access_token = result["access_token"]
                self.refresh_token = result["refresh_token"]
                await self._store_credentials()
                return True
        except aiohttp.ClientResponseError as error:
            if error.status != 401:
                raise
            print(
                "Failed to refresh access token, fetching new tokens using credentials"
            )
            await self._fetch_tokens()
            return True
        except Exception as e:
            print(f"Error refreshing token: {e}")
            return False

    async def _request_protobuf(
        self,
        method,
        path,
        protobuf_response_class=None,
        data=None,
        as_form=False,
        params=None,
        auth_required=True,
    ):
        """Make a request to the AnyList API expecting a protobuf response.

        Args:
            method: HTTP method (get, post, put, delete)
            path: API endpoint path (without base URL)
            protobuf_response_class: The protobuf message class to use for decoding the response (required)
            data: Request JSON data (for POST/PUT)
            params: Query parameters
            auth_required: Whether authentication is required

        Returns:
            Response data as decoded protobuf dictionary
        """
        if auth_required and not self.access_token:
            await self.login()

        url = f"{self.BASE_URL}/{path.lstrip('/')}"

        # Get authentication headers
        _headers = self._get_auth_headers(auth_required)

        try:
            request_method = getattr(self.session, method.lower())
            request_kwargs = {"params": params, "headers": _headers}

            if data:
                if as_form:
                    form_data = aiohttp.FormData(default_to_multipart=True)
                    for key, value in data.items():
                        # form_data.add_field(key, value)
                        # ^ sets the filename in the encoded data, which breaks anylist, so do it manually
                        type_options = MultiDict({"name": key})
                        headers = {}
                        form_data._fields.append((type_options, headers, value))
                    request_kwargs["data"] = form_data
                else:
                    request_kwargs["json"] = data

            async with request_method(url, **request_kwargs) as resp:
                resp.raise_for_status()

                if protobuf_response_class is not None:
                    binary_data = await resp.read()

                    pb_message = protobuf_response_class()
                    pb_message.ParseFromString(binary_data)

                    return pb_message
                else:
                    return True

        except aiohttp.ClientResponseError as error:
            if auth_required and error.status == 401:
                # Token expired, refresh and try again
                await self._refresh_tokens()
                return await self._request_protobuf(
                    method,
                    path,
                    protobuf_response_class,
                    data,
                    as_form,
                    params,
                    auth_required,
                )
            raise

    async def get_lists(self):
        """Get all user lists.

        This fetches all user data and extracts the lists.
        """
        user_data = await self.get_user_data()
        return [
            ShoppingList(self, item)
            for item in user_data.shoppingListsResponse.newLists
        ]

    async def get_list_by_name(self, name):
        lists = await self.get_lists()
        for lst in lists:
            if lst.name.lower() == name.lower():
                return lst
        return None

    def _get_auth_headers(self, auth_required=True):
        _headers = {
            "X-AnyLeaf-API-Version": "3",
        }

        if auth_required and self.access_token:
            _headers["Authorization"] = f"Bearer {self.access_token}"
            _headers["X-AnyLeaf-Client-Identifier"] = self.client_id

        return _headers

    async def _get_client_id(self):
        """Get or generate a client ID."""
        if self.client_id:
            return self.client_id
        print("No saved clientId found, generating new clientId")

        self.client_id = str(uuid.uuid4())
        await self._store_credentials()
        return self.client_id

    async def _load_credentials(self):
        """Load credentials from the credentials file."""
        if not self.credentials_file or not os.path.exists(self.credentials_file):
            print("Credentials file does not exist, not loading saved credentials")
            return
        try:
            with open(self.credentials_file, "r") as f:
                encrypted = f.read()
                credentials = decrypt_credentials(encrypted, self.password)
                self.client_id = credentials.get(CREDENTIALS_KEY_CLIENT_ID)
                self.access_token = credentials.get(CREDENTIALS_KEY_ACCESS_TOKEN)
                self.refresh_token = credentials.get(CREDENTIALS_KEY_REFRESH_TOKEN)
        except Exception as error:
            print(f"Failed to read stored credentials: {error}")

    async def _store_credentials(self):
        """Store credentials in the credentials file."""
        if not self.credentials_file:
            return
        credentials = {
            CREDENTIALS_KEY_CLIENT_ID: self.client_id,
            CREDENTIALS_KEY_ACCESS_TOKEN: self.access_token,
            CREDENTIALS_KEY_REFRESH_TOKEN: self.refresh_token,
        }
        try:
            encrypted = encrypt_credentials(credentials, self.password)
            with open(self.credentials_file, "w") as f:
                f.write(encrypted)
        except Exception as error:
            print(f"Failed to write credentials to storage: {error}")

    def create_item(self) -> ShoppingListItem:
        """Create a new shopping list item."""
        return ShoppingListItem(self, None)
