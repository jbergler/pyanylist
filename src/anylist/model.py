import typing
from uuid import uuid4

from anylist import messages_pb2 as pb

if typing.TYPE_CHECKING:
    from anylist.client import AnyListClient


def uuid() -> str:
    return str(uuid4()).replace("-", "")


class ShoppingList:
    def __init__(self, client: "AnyListClient", lst: pb.ShoppingList):
        self.client = client
        self.identifier = lst.identifier
        self.name = lst.name
        self.uid = lst.creator
        self.items = [ShoppingListItem(client, item) for item in lst.items]

    def __repr__(self):
        return f"List(id={self.identifier}, name={self.name})"

    async def find_item_by_name(self, name: str) -> "ShoppingListItem" | None:
        return next(
            filter(lambda item: item.name.lower() == name.lower(), self.items), None
        )

    async def add_item(self, item: "ShoppingListItem"):
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
        self.listId = item.listId if item else None
        self.identifier = item.identifier if item else uuid()
        self.name = item.name if item else ""
        self.details = item.details if item else ""
        self.quantity = item.quantityPb.amount if item else "1"
        self.checked = item.checked if item else False
        self.category = item.categoryMatchId if item else "other"
        self.userId = item.userId if item else client.uid
        self.client.user_data.userCategoriesResponse.categories

    def encode(self) -> pb.ListItem:
        """Encode the item to a protobuf message."""
        return pb.ListItem(
            identifier=self.identifier,
            listId=self.listId,
            name=self.name,
            userId=self.userId,
            category=self.category,
            details=self.details,
            quantityPb=pb.PBItemQuantity(amount=self.quantity),
            checked=self.checked,
        )
