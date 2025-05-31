# from pydantic import BaseModel

# class ListItem(BaseModel):
#     id: str
#     name: str
#     description: str = ""
#     completed: bool = False

# class ShoppingListStub(BaseModel):
#     id: str
#     name: str

# class ShoppingList(ShoppingListStub):
#     items: list[ListItem]

from uuid import uuid4
from . import messages_pb2 as pb

def uuid() -> str:
    return str(uuid4()).replace('-', '')

class ShoppingList:
    def __init__(self, list: pb.ShoppingList):
        self.id = list.identifier
        self.name = list.name
        self.items = [ShoppingListItem(item) for item in list.items]

    def __repr__(self):
        return f"List(id={self.id}, name={self.name})"
    
class ShoppingListItem:
    def __init__(self, item: pb.ListItem | None):
        self.id = item.identifier if item else uuid()
        self.name = item.name if item else ""
        self.details = item.details if item else ""
        self.quantity = item.quantityPb.amount if item else "1"
        self.checked = item.checked if item else False
