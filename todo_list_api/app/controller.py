from typing import List

from todo_list_api.db.interface import DataBase
from todo_list_api.model.list import TodoList


class TodoListController:
    """
    A helper class that makes it easy to retrieve and store new TodoLists
    """

    def __init__(self, database: DataBase):
        self.database: DataBase = database
        self.database.setup()

    def get_lists(self) -> List[TodoList]:
        """
        Return all TodoLists
        :return: A list of TodoLists
        """
        return self.database.get_lists()

    def get_list(self, name: str) -> TodoList:
        """
        Return the TodoList with given name
        :param name: the name of the TodoList
        :return: The TodoList
        """
        return self.database.get_list(name)

    def create_list(self, name) -> TodoList:
        """
        Create a new TodoList
        :param name: The name of the list
        :return: A new Todo List
        """
        return self.database.create_list(name)

    def delete_list(self, name: str) -> None:
        """
        Delete a list with given name
        :param name:
        :return:
        """
        return self.database.delete_list(name)

    def add_item(self, list_name: str, item_name: str, item_description: str) -> None:
        """
        Add an Item to the TodoList
        :param list_name: The name of the TodoList
        :param item_name: The name of the item
        :param item_description: The description of the Item
        :return: None
        """
        return self.database.add_item(list_name, item_name, item_description)

    def delete_item(self, list_name: str, item_name: str) -> None:
        """
        Delete an item from a TodoList
        :param list_name: The name of the list
        :param item_name: The index of the item in the list
        :return: None
        """
        return self.database.delete_item(list_name, item_name)
