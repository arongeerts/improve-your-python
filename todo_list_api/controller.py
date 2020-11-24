from typing import Dict, List

from todo_list_api.exceptions import HTTPException
from todo_list_api.model.item import Item
from todo_list_api.model.list import TodoList


class TodoListController:
    """
    A helper class that makes it easy to retrieve and store new TodoLists
    """

    def __init__(self):
        self.lists: Dict[str, TodoList] = {}  # stored by name

    def get_lists(self) -> List[TodoList]:
        """
        Return all TodoLists
        :return: A list of TodoLists
        """
        return list(self.lists.values())

    def get_list(self, name: str) -> TodoList:
        """
        Return the TodoList with given name
        :param name: the name of the TodoList
        :return: The TodoList
        """
        list_ = self.lists.get(self.__to_key(name))
        if not list_:
            raise HTTPException(
                404,
                f"No TODO list with name {name}"
            )
        return list_

    def create_list(self, name, description) -> TodoList:
        """
        Create a new TodoList
        :param name: The name of the list
        :param description: the description
        :return: A new Todo List
        """
        t = TodoList(name, description)
        if name in self.lists:
            raise HTTPException(
                409,
                f"TODO list with name {name} already exists"
            )
        self.lists[self.__to_key(name)] = t
        return t

    def delete_list(self, name: str) -> None:
        """
        Delete a list with given name
        :param name:
        :return:
        """
        if name in self.lists:
            del self.lists[self.__to_key(name)]
        else:
            raise HTTPException(
                404,
                f"No TODO list with name {name}"
            )

    def add_item(self, list_name: str, item_name: str, item_description: str) -> None:
        """
        Add an Item to the TodoList
        :param list_name: The name of the TodoList
        :param item_name: The name of the item
        :param item_description: The description of the Item
        :return: None
        """
        todo_list = self.get_list(list_name)
        todo_list.add_item(Item(item_name, item_description))

    def delete_item(self, list_name: str, index: int) -> None:
        """
        Delete an item from a TodoList
        :param list_name: The name of the list
        :param index: The index of the item in the list
        :return: None
        """
        todo_list = self.get_list(list_name)
        todo_list.delete_item(index)

    @staticmethod
    def __to_key(name: str) -> str:
        """
        Create a key without spaces that can be used as a URL parameter
        :param name: The original name of the TodoList
        :return:
        """
        return name.replace(" ", "-")
