"""API Client code"""

from __future__ import annotations

import functools
from typing import Self, Any, Dict, List, Optional
import os
import json
import uuid

import aiohttp

from pyanylist.model import ShoppingList

from .credentials import (
    CREDENTIALS_KEY_CLIENT_ID,
    CREDENTIALS_KEY_ACCESS_TOKEN,
    CREDENTIALS_KEY_REFRESH_TOKEN,
    encrypt_credentials,
    decrypt_credentials,
)
from . import messages_pb2

__all__ = [
    "AnyListClient",
]

class AnyListClient:
    """Client for interacting with the AnyList API."""
    
    BASE_URL = "https://www.anylist.com"
    
    def __init__(self, email, password, credentials_file=None):
        self.email = email
        self.password = password
        self.credentials_file = credentials_file or os.path.expanduser("~/.anylist_credentials")
        self.access_token = None
        self.refresh_token = None
        self.client_id = None
        self.session = None
        self.user_data: messages_pb2.PBUserDataResponse | None = None

    async def __aenter__(self):
        """Enter the async context manager, creating a session."""
        self.session = aiohttp.ClientSession(
            headers=self._get_auth_headers(auth_required=False)
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
            
    async def get_user_data(self, refresh=False) -> messages_pb2.PBUserDataResponse:
        """Get all user data from AnyList using the data/user-data/get endpoint.
        
        This is the primary method to fetch user data from AnyList. It returns a
        dictionary with all user data including lists, items, recipes, etc.
        """
        if self.user_data and not refresh:
            return self.user_data
        
        self.user_data = await self._request_protobuf(
            "post", 
            "data/user-data/get", 
            protobuf_response_class=messages_pb2.PBUserDataResponse
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
            print("Failed to refresh access token, fetching new tokens using credentials")
            await self._fetch_tokens()
            return True
        except Exception as e:
            print(f"Error refreshing token: {e}")
            return False
    
    async def _request_protobuf(self, method, path, protobuf_response_class, data=None, params=None, auth_required=True):
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
            
            # Add JSON data if provided
            if data:
                request_kwargs["json"] = data
                
            async with request_method(url, **request_kwargs) as resp:
                resp.raise_for_status()

                binary_data = await resp.read()

                pb_message = protobuf_response_class()
                pb_message.ParseFromString(binary_data)
                return pb_message
 
                
        except aiohttp.ClientResponseError as error:
            if auth_required and error.status == 401:
                # Token expired, refresh and try again
                await self._refresh_tokens()
                return await self._request_protobuf(method, path, protobuf_response_class, data, params, auth_required)
            raise
            
    def _protobuf_to_dict(self, message):
        """Convert a protobuf message to a dictionary.
        
        This method handles the most common protobuf types, including nested
        messages, repeated fields, and scalar values.
        
        Args:
            message: The protocol buffer message to convert
            
        Returns:
            A dictionary representation of the message
        """
        result = {}
        for field, value in message.ListFields():
            if field.label == field.LABEL_REPEATED:
                # Handle repeated fields (lists)
                if field.type == field.TYPE_MESSAGE:
                    # Repeated message field
                    result[field.name] = [self._protobuf_to_dict(item) for item in value]
                else:
                    # Repeated scalar field
                    result[field.name] = list(value)
            elif field.type == field.TYPE_MESSAGE:
                # Handle nested message
                result[field.name] = self._protobuf_to_dict(value)
            else:
                # Handle scalar field
                result[field.name] = value
        return result
    
    async def get_lists(self):
        """Get all user lists.
        
        This fetches all user data and extracts the lists.
        """
        user_data = await self.get_user_data()
        return [
            ShoppingList(item)
            for item in user_data.shoppingListsResponse.newLists
        ]
    
    async def get_list_items(self, list_id):
        """Get items in a specific list.
        
        Args:
            list_id: The ID of the list to get items from
            
        Returns:
            List of items in the specified list
        """
        # In the AnyList API, list items are included in the user data
        user_data = await self.get_user_data()
        lists = user_data.shoppingListsResponse.newLists
        for lst in lists:
            if lst.get("listId") == list_id:
                return lst.get("items", [])
        return []

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
