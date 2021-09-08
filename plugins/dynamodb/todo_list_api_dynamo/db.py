import os
from typing import List, Dict, Any

import boto3
from todo_list_api.app.exceptions import ListNotFoundException
from todo_list_api.db.interface import DataBase
from todo_list_api.model.item import Item
from todo_list_api.model.list import TodoList


class TodoListDynamoDB(DataBase):
    def __init__(self):
        super().__init__()
        self.table_name = os.environ["DYNAMODB_TABLE"]
        region_name = os.environ["DYNAMODB_REGION"]
        endpoint_url = os.environ.get("DYNAMODB_ENDPOINT")

        params = {"region_name": region_name}
        if endpoint_url:
            params["endpoint_url"] = endpoint_url
        self.client = boto3.client("dynamodb", **params)

    def get_lists(self) -> List[TodoList]:
        items = self.client.scan(TableName=self.table_name).get("Items", [])
        return [self.parse_todo_list(item) for item in items]

    def get_list(self, name: str) -> TodoList:
        key = self.__get_key(name)
        item = self.client.get_item(Key=key, TableName=self.table_name).get("Item")
        if not item:
            raise ListNotFoundException(name)
        return self.parse_todo_list(item)

    def create_list(self, name: str) -> TodoList:
        todo_list = TodoList(name, [])
        self.__save_list(todo_list)
        return todo_list

    def delete_list(self, name: str) -> None:
        key = self.__get_key(name)
        self.client.delete_item(Key=key, TableName=self.table_name)

    def add_item(self, list_name: str, item_name: str, item_description: str) -> None:
        key = self.__get_key(list_name)
        self.client.update_item(
            TableName=self.table_name,
            Key=key,
            UpdateExpression="SET todo_items = list_append(todo_items, :i)",
            ExpressionAttributeValues={
                ":i": {
                    "L": [
                        {
                            "M": {
                                "name": {"S": item_name},
                                "description": {"S": item_description},
                            }
                        }
                    ]
                }
            },
        )

    def delete_item(self, list_name: str, item_name: str) -> None:
        todo_list = self.get_list(list_name)
        for index, item in enumerate(todo_list.items):
            if item.name == item_name:
                todo_list.delete_item(index)
        self.__save_list(todo_list)

    @staticmethod
    def __to_item(todo_list: TodoList):
        return {
            "name": {"S": todo_list.name},
            "todo_items": {
                "L": [
                    {"M": {"name": {"S": i.name}, "description": {"S": i.description}}}
                    for i in todo_list.items
                ]
            },
        }

    def __save_list(self, todo_list: TodoList):
        self.client.put_item(Item=self.__to_item(todo_list), TableName=self.table_name)

    @staticmethod
    def __get_key(name: str) -> Dict[str, Dict[str, str]]:
        return {"name": {"S": name}}

    @staticmethod
    def parse_todo_list(item: Dict[str, Dict[str, Any]]) -> TodoList:
        return TodoList(
            item["name"]["S"],
            [TodoListDynamoDB.parse_list_item(i["M"]) for i in item["todo_items"]["L"]],
        )

    @staticmethod
    def parse_list_item(item: Dict[str, Dict[str, Any]]) -> Item:
        return Item(item["name"]["S"], item["description"]["S"])

    def setup(self):
        try:
            self.client.create_table(
                TableName=self.table_name,
                KeySchema=[
                    {
                        "AttributeName": "name",
                        "KeyType": "HASH",
                    }
                ],
                AttributeDefinitions=[
                    {"AttributeName": "name", "AttributeType": "S"},
                ],
                ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
            )
        except:
            pass
