import os
from abc import ABC, abstractmethod
from typing import List

from todo_list_api.app.plugin import Plugin
from todo_list_api.model.list import TodoList


class DataBase(Plugin, ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_lists(self) -> List[TodoList]:
        """
        Return all the TodoLists in the Database as a list
        :return: A List of TodoList's
        """

    @abstractmethod
    def get_list(self, name: str) -> TodoList:
        """
        Get one TodoList by name
        :param name: The name of the list
        :return: a TodoList
        """

    @abstractmethod
    def create_list(self, name: str) -> TodoList:
        """
        Create a new TodoList
        :param name: The name of the TodoList
        :return: A new TodoList object
        """

    @abstractmethod
    def delete_list(self, name: str) -> None:
        """
        Delete a list with given name from the Database
        :param name:
        :return: Nothing
        """

    @abstractmethod
    def add_item(self, list_name: str, item_name: str, item_description: str) -> None:
        """
        Add an Item to the TodoList
        :param list_name: The name of the TodoList
        :param item_name: The name of the item
        :param item_description: The description of the Item
        :return: None
        """

    @abstractmethod
    def delete_item(self, list_name: str, item_name: str) -> None:
        """
        Delete an item from a TodoList
        :param list_name: The name of the list
        :param item_name: The name of the item
        :return: None
        """

    @abstractmethod
    def setup(self):
        """
        Setup the necessary resources in the Database
        """

    @classmethod
    def get_class_reference(cls) -> str:
        return os.environ.get(
            "TODO_LIST_DB_IMPLEMENTATION", "todo_list_api.db.memory.InMemoryDatabase"
        )
