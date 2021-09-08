import os
from time import sleep
from typing import List

import mysql.connector as mysql

from todo_list_api.app.exceptions import HTTPException
from todo_list_api.db.interface import DataBase
from todo_list_api.model.item import Item
from todo_list_api.model.list import TodoList


def init_connection():
    """
    Initialize a connection to the database.
    As this is a persistent connection, we will initialize this only once for the entire python process
    """
    sleep(10)
    host = os.environ["MYSQL_HOST"]
    user = os.environ["MYSQL_USER"]
    password = os.environ["MYSQL_PASSWORD"]
    database = os.environ["MYSQL_DATABASE"]
    connection = mysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        auth_plugin="mysql_native_password",
    )
    return connection


class TodoListMySQL(DataBase):

    connection = init_connection()

    def __init__(self):
        super().__init__()

    def get_lists(self) -> List[TodoList]:
        query = (
            "SELECT l.name, i.item_name, i.item_description "
            "FROM todo_lists l "
            "LEFT JOIN todo_items i "
            "ON l.name = i.list_name;"
        )
        cursor = self.connection.cursor()
        cursor.execute(query)
        items = {}
        for row in cursor.fetchall():
            if row[0] not in items:
                items[row[0]] = TodoList(
                    name=row[0], items=[Item(name=row[1], description=row[2])]
                )
            else:
                items[row[0]].add_item(Item(name=row[1], description=row[2]))
        cursor.close()
        return list(items.values())

    def get_list(self, name: str) -> TodoList:
        query = (
            "SELECT l.name, i.item_name, i.item_description "
            "FROM todo_lists l "
            "LEFT JOIN todo_items i "
            "ON l.name = i.list_name "
            "WHERE l.name = '%s';"
        )
        cursor = self.connection.cursor()
        cursor.execute(query % (name,))

        if len(cursor.fetchall()) == 0:
            raise HTTPException(
                status_code=404, reason=f"No list found with name '{name}'"
            )

        todo_list = TodoList(name, items=[])
        for row in cursor.fetchall():
            todo_list.add_item(Item(name=row[1], description=row[2]))
        cursor.close()
        return todo_list

    def create_list(self, name: str) -> TodoList:
        item = TodoList(name, [])
        query = "INSERT INTO todo_lists VALUES ('%s');"

        cursor = self.connection.cursor()
        cursor.execute(query % (name,))
        cursor.close()
        return item

    def delete_list(self, name: str) -> None:
        query_lists = "DELETE FROM todo_lists WHERE name = '%s';"
        query_items = "DELETE FROM todo_items WHERE list_name = '%s';"
        cursor = self.connection.cursor()
        cursor.execute(query_lists % (name,))
        cursor.execute(query_items % (name,))
        cursor.close()

    def add_item(self, list_name: str, item_name: str, item_description: str) -> None:
        query = "INSERT INTO todo_items VALUES ('%s', '%s', '%s');"
        cursor = self.connection.cursor()
        cursor.execute(query % (list_name, item_name, item_description))
        cursor.close()

    def delete_item(self, list_name: str, item_name: str) -> None:
        query = "DELETE FROM todo_items WHERE list_name = '%s' AND item_name = '%s';"
        cursor = self.connection.cursor()
        cursor.execute(query % (list_name, item_name))
        cursor.close()

    def setup(self):
        create_db = f"CREATE DATABASE IF NOT EXISTS todo;"
        query_lists = (
            "CREATE TABLE IF NOT EXISTS todo_lists (" "  name VARCHAR(100)" ");"
        )
        query_items = (
            "CREATE TABLE IF NOT EXISTS todo_items ("
            "  list_name VARCHAR(100), "
            "  item_name VARCHAR(100), "
            "  item_description VARCHAR(10000)"
            ");"
        )
        cursor = self.connection.cursor()
        cursor.execute(create_db)
        cursor.execute(query_items)
        cursor.execute(query_lists)
        cursor.close()
