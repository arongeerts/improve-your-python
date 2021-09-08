from unittest import TestCase

from todo_list_api.app.controller import TodoListController
from todo_list_api.app.exceptions import HTTPException
from todo_list_api.db.memory import InMemoryDatabase


class TestController(TestCase):
    def test_create_list(self):
        controller = TodoListController(InMemoryDatabase())
        controller.create_list("A test list")
        got = controller.get_lists()
        self.assertEqual(1, len(got))

    def test_get_lists_no_list(self):
        controller = TodoListController(InMemoryDatabase())
        got = controller.get_lists()
        self.assertEqual([], got)

    def test_get_lists_with_list(self):
        controller = TodoListController(InMemoryDatabase())
        controller.create_list("A test list")
        got = controller.get_lists()
        self.assertEqual(1, len(got))

    def test_get_list_by_name(self):
        controller = TodoListController(InMemoryDatabase())
        controller.create_list("A test list")
        got = controller.get_list("A test list")
        self.assertIsNotNone(got)

    def test_get_non_existing_list_404(self):
        controller = TodoListController(InMemoryDatabase())
        self.assertRaises(HTTPException, controller.get_list, "A non existing list")

    def test_delete_list(self):
        controller = TodoListController(InMemoryDatabase())
        controller.create_list("A test list")
        got = controller.get_lists()
        self.assertEqual(1, len(got))
        controller.delete_list("A test list")
        got = controller.get_lists()
        self.assertEqual([], got)

    def test_add_item(self):
        controller = TodoListController(InMemoryDatabase())
        controller.create_list("A test list")
        controller.add_item("A test list", "Item 1", "A new item")
        l = controller.get_list("A test list")
        got = l.items[0]
        self.assertEqual("Item 1", got.name)

    def test_delete_item(self):
        controller = TodoListController(InMemoryDatabase())
        controller.create_list("A test list")
        controller.add_item("A test list", "Item 1", "A new item")
        l = controller.get_list("A test list")
        got = l.items[0]
        self.assertEqual("Item 1", got.name)
        controller.delete_item("A test list", "Item 1")
        l = controller.get_list("A test list")
        self.assertEqual([], l.items)
