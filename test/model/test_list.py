import copy
from unittest import TestCase

from todo_list_api.model.item import Item
from todo_list_api.model.list import TodoList


class TestList(TestCase):
    example_list = TodoList(
        name="My Todo list",
        items=[
            Item(name="Item 1", description="The first item on the list"),
            Item(name="Item 2", description="The second item on the list"),
        ],
    )

    def test_dict(self):
        expected = {
            "name": "My Todo list",
            "items": [
                {"name": "Item 1", "description": "The first item on the list"},
                {"name": "Item 2", "description": "The second item on the list"},
            ],
        }
        got = self.example_list.dict()
        self.assertEqual(expected, got)

    def test_json(self):
        expected = (
            '{"name": "My Todo list", '
            '"items": [{"name": "Item 1", "description": "The first item on the list"}, '
            '{"name": "Item 2", "description": "The second item on the list"}]}'
        )
        got = self.example_list.json()
        self.assertEqual(expected, got)

    def test_from_json(self):
        i = (
            '{"name": "My Todo list", '
            '"items": [{"name": "Item 1", "description": "The first item on the list"}, '
            '{"name": "Item 2", "description": "The second item on the list"}]}'
        )
        got = TodoList.from_json(i)
        self.assertEqual(self.example_list, got)

    def test_add_item(self):
        o = copy.deepcopy(self.example_list)
        o.add_item(Item(name="Item 3", description="The third item on the list"))
        self.assertEqual(len(o.items), 3)
        self.assertEqual(o.items[2].name, "Item 3")

    def test_delete_item(self):
        o = copy.deepcopy(self.example_list)
        o.delete_item(0)
        self.assertEqual(len(o.items), 1)
        self.assertEqual(o.items[0].name, "Item 2")
