from __future__ import annotations

import json
from typing import Any, Dict


class Item:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def dict(self) -> Dict[str, Any]:
        """
        Create a dictionary from the given item
        :return: A dictionary
        """
        return {"name": self.name, "description": self.description}

    def json(self) -> str:
        """
        Return a json string that represents the current item
        :return: A Json string
        """
        return json.dumps(self.dict())

    @classmethod
    def from_json(cls, s: str) -> Item:
        """
        Return an Item object from a JSON string
        :param s: The JSON representation of the Item
        :return: An Item object
        """
        return cls(**json.loads(s))

    def __eq__(self, other):
        if not isinstance(other, Item):
            return False
        return self.name == other.name and self.description == other.description
