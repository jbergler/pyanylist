import typing
from uuid import uuid4

from anylist import messages_pb2 as pb

if typing.TYPE_CHECKING:
    from anylist.client import AnyListClient


def uuid() -> str:
    return str(uuid4()).replace("-", "")


# Operation mapping for item fields to API handlers
OP_MAPPING = {
    "name": "set-list-item-name",
    "quantity": "set-list-item-quantity",
    "details": "set-list-item-details",
    "checked": "set-list-item-checked",
    "category": "set-list-item-category-match-id",
    "manualSortIndex": "set-list-item-sort-order",
}


class ShoppingList:
    def __init__(self, client: "AnyListClient", lst: pb.ShoppingList):
        self.client = client
        self.identifier = lst.identifier
        self.name = lst.name
        self.uid = lst.creator
        self.items = [ShoppingListItem(client, item) for item in lst.items]

    def __repr__(self):
        return f"List(id={self.identifier}, name={self.name})"

    async def find_item_by_name(self, name: str) -> typing.Optional["ShoppingListItem"]:
        return next(
            filter(lambda item: item.name.lower() == name.lower(), self.items), None
        )

    async def add_item(self, item: "ShoppingListItem"):
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


class ShoppingListItem:
    def __init__(self, client: "AnyListClient", item: pb.ListItem | None):
        self.client = client
        self._listId = item.listId if item else None
        self._identifier = item.identifier if item else uuid()
        self._name = item.name if item else ""
        self._details = item.details if item else ""
        self._quantity = item.quantityPb.amount if item else "1"
        self._checked = item.checked if item else False
        self._category = item.categoryMatchId if item else "other"
        self._userId = item.userId if item else client.uid
        self._manualSortIndex = getattr(item, "manualSortIndex", None)
        self._fields_to_update = []

    @property
    def identifier(self) -> str:
        return self._identifier

    @identifier.setter
    def identifier(self, value):
        raise ValueError("You cannot update an item ID.")

    @property
    def listId(self) -> str:
        return self._listId

    @listId.setter
    def listId(self, value):
        if self._listId is None:
            self._listId = value
            self._fields_to_update.append("listId")
        else:
            raise ValueError("You cannot move items between lists.")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._fields_to_update.append("name")

    @property
    def quantity(self) -> str:
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, (int, float)):
            value = str(value)
        self._quantity = value
        self._fields_to_update.append("quantity")

    @property
    def details(self) -> str:
        return self._details

    @details.setter
    def details(self, value):
        self._details = value
        self._fields_to_update.append("details")

    @property
    def checked(self) -> bool:
        return self._checked

    @checked.setter
    def checked(self, value):
        if not isinstance(value, bool):
            raise TypeError("Checked must be a boolean.")
        self._checked = value
        self._fields_to_update.append("checked")

    @property
    def userId(self) -> str:
        return self._userId

    @userId.setter
    def userId(self, value):
        if self._userId:
            raise ValueError("Cannot set user ID of an item after creation.")
        self._userId = value

    @property
    def category(self) -> str:
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
        self._fields_to_update.append("category")

    @property
    def manualSortIndex(self):
        return self._manualSortIndex

    @manualSortIndex.setter
    def manualSortIndex(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Sort index must be a number.")
        self._manualSortIndex = value
        self._fields_to_update.append("manualSortIndex")

    def encode(self) -> pb.ListItem:
        """Encode the item to a protobuf message."""
        return pb.ListItem(
            identifier=self._identifier,
            listId=self._listId,
            name=self._name,
            userId=self._userId,
            categoryMatchId=self._category,
            details=self._details,
            quantityPb=pb.PBItemQuantity(amount=self._quantity),
            checked=self._checked,
            manualSortIndex=self._manualSortIndex,
        )

    async def save(self, is_favorite: bool = False) -> None:
        """
        Save local changes to item to AnyList's API.

        Args:
            is_favorite: Must set to True if editing "favorites" list
        """
        operations = []

        for field in self._fields_to_update:
            if field not in OP_MAPPING:
                continue

            value = getattr(self, field)
            handler_id = OP_MAPPING[field]

            # Convert boolean to y/n for API
            if isinstance(value, bool):
                updated_value = "y" if value else "n"
            else:
                updated_value = str(value)

            op = pb.PBListOperation(
                listId=self._listId,
                listItemId=self._identifier,
                metadata=pb.PBOperationMetadata(
                    operationId=uuid(),
                    handlerId=handler_id,
                    userId=self._userId,
                ),
                updatedValue=updated_value,
            )

            operations.append(op)

        if not operations:
            return

        ops = pb.PBListOperationList(
            operations=operations,
        )

        path = (
            "data/starter-lists/update" if is_favorite else "data/shopping-lists/update"
        )

        await self.client._request_protobuf(
            method="POST",
            path=path,
            data={"operations": ops.SerializeToString()},
            as_form=True,
            auth_required=True,
        )

        # Clear the fields to update after saving
        self._fields_to_update = []
