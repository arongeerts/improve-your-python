from unittest import TestCase

from todo_list_api.controller import TodoListController
from todo_list_api.exceptions import HTTPException
from todo_list_api.model.item import Item
from todo_list_api.model.list import TodoList


class TestController(TestCase):
    example_list = TodoList(
        name="My Todo list",
        items=[
            Item(name="Item 1", description="The first item on the list"),
            Item(name="Item 2", description="The second item on the list"),
        ],
    )

    def test_create_list(self):
        controller = TodoListController()
        controller.create_list("A test list")
        got = controller.get_lists()
        self.assertEqual(1, len(got))

    def test_get_lists_no_list(self):
        controller = TodoListController()
        got = controller.get_lists()
        self.assertEqual([], got)

    def test_get_lists_with_list(self):
        controller = TodoListController()
        controller.create_list("A test list")
        got = controller.get_lists()
        self.assertEqual(1, len(got))

    def test_get_list_by_name(self):
        controller = TodoListController()
        controller.create_list("A test list")
        got = controller.get_list("A test list")
        self.assertIsNotNone(got)

    def test_get_non_existing_list_404(self):
        controller = TodoListController()
        self.assertRaises(HTTPException, controller.get_list, "A non existing list")

    def test_delete_list(self):
        controller = TodoListController()
        controller.create_list("A test list")
        got = controller.get_lists()
        self.assertEqual(1, len(got))
        controller.delete_list("A test list")
        got = controller.get_lists()
        self.assertEqual([], got)

    def test_add_item(self):
        controller = TodoListController()
        controller.create_list("A test list")
        controller.add_item("A test list", "Item 1", "A new item")
        l = controller.get_list("A test list")
        got = l.items[0]
        self.assertEqual("Item 1", got.name)

    def test_delete_item(self):
        controller = TodoListController()
        controller.create_list("A test list")
        controller.add_item("A test list", "Item 1", "A new item")
        l = controller.get_list("A test list")
        got = l.items[0]
        self.assertEqual("Item 1", got.name)
        controller.delete_item("A test list", 0)
        l = controller.get_list("A test list")
        self.assertEqual([], l.items)
