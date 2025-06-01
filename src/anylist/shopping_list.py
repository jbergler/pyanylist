"""ShoppingList class for AnyList API."""

import typing

from anylist import messages_pb2 as pb
from anylist.common import uuid
from anylist.shopping_list_item import ShoppingListItem

if typing.TYPE_CHECKING:
    from anylist.client import AnyListClient


class ShoppingList:
    """
    Represents an AnyList shopping list.

    Provides methods to interact with lists and their items.
    """

    def __init__(self, client: "AnyListClient", lst: pb.ShoppingList):
        self.client = client
        self.identifier = lst.identifier
        self.name = lst.name
        self.uid = lst.creator
        self.items = [ShoppingListItem(client, item) for item in lst.items]

    def __repr__(self):
        return f"List(id={self.identifier}, name={self.name})"

    async def find_item_by_name(self, name: str) -> typing.Optional[ShoppingListItem]:
        """
        Find an item in the list by name (case-insensitive).

        Args:
            name: The name of the item to find

        Returns:
            The item if found, None otherwise
        """
        return next(
            filter(lambda item: item.name.lower() == name.lower(), self.items), None
        )

    async def add_item(self, item: ShoppingListItem):
        """
        Add an item to the list.

        If an item with the same name already exists and is checked,
        it will be unchecked instead of adding a new item.

        Args:
            item: The item to add to the list
        """
        if existing := await self.find_item_by_name(item.name):
            if existing.checked:
                existing.checked = False
                await existing.save()
            return

        item.listId = self.identifier
        item.userId = self.uid

        op = pb.PBListOperation(
            listId=self.identifier,
            listItemId=item.identifier,
            listItem=item.encode(),
            metadata=pb.PBOperationMetadata(
                operationId=uuid(),
                handlerId="add-shopping-list-item",
                userId=item.userId,
            ),
        )

        ops = pb.PBListOperationList(
            operations=[op],
        )

        await self.client._request_protobuf(
            method="POST",
            path="data/shopping-lists/update",
            data={"operations": ops.SerializeToString()},
            as_form=True,
            auth_required=True,
        )
        self.items.append(item)
