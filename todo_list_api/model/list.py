from __future__ import annotations

import json
from typing import Any, Dict, List

from todo_list_api.model.item import Item


class TodoList:
    def __init__(self, name: str, items: List[Item]):
        self.name = name
        self.items = items

    def dict(self) -> Dict[str, Any]:
        """
        Return a dict from the current TodoList
        :return: A Dictionary
        """
        return {"name": self.name, "items": [i.dict() for i in self.items]}

    def json(self):
        """
        Return a JSON string from this TodoList
        :return:
        """
        return json.dumps(self.dict())

    @classmethod
    def from_json(cls, s: str) -> TodoList:
        """
        Create a TodoList object from a JSON string
        :param s: The JSON representation of the TodoList
        :return: A TodoList object
        """
        d = json.loads(s)
        items = [Item(**d["items"][i]) for i in range(len(d["items"]))]
        return cls(name=d["name"], items=items)

    def add_item(self, item: Item):
        """
        Add an Item to this TodoList
        :param item: The Item to add
        :return: None
        """
        self.items.append(item)

    def delete_item(self, index: int):
        """
        Delete an item from this TodoList
        :param index: The number of the item to delete
        :return:
        """
        del self.items[index]

    def __eq__(self, other):
        if not isinstance(other, TodoList):
            return False
        return self.json() == other.json()
