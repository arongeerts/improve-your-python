from unittest import TestCase

from todo_list_api.api import app


class TestApi(TestCase):
    def test_post_list(self):
        client = app.test_client()
        response = client.post("/lists", json={"name": "A list"})
        self.assertEqual(response.status_code, 200)

    def test_get_lists(self):
        client = app.test_client()
        client.post("/lists", json={"name": "A list"})
        response = client.get("/lists")
        self.assertEqual(response.status_code, 200)
        lists = response.json["body"]
        self.assertEqual(len(lists), 1)
        name = lists[0]["name"]
        self.assertEqual(name, "A list")

    def test_get_one_list(self):
        client = app.test_client()
        client.post("/lists", json={"name": "A list"})
        response = client.get("/lists/A-list")
        self.assertEqual(response.status_code, 200)
        lists = response.json["body"]
        name = lists["name"]
        self.assertEqual(name, "A list")

    def test_add_item(self):
        client = app.test_client()
        client.post("/lists", json={"name": "A list"})
        client.post(
            "/lists/A-list/item",
            json={"name": "An Item", "description": "An item to do"},
        )
        response = client.get("/lists/A-list")
        self.assertEqual(response.status_code, 200)
        lists = response.json["body"]
        items = lists["items"]
        self.assertEqual(len(items), 1)

    def test_delete_item(self):
        client = app.test_client()
        client.post("/lists", json={"name": "A list"})
        client.post(
            "/lists/A-list/item",
            json={"name": "An Item", "description": "An item to do"},
        )
        response = client.get("/lists/A-list")
        self.assertEqual(response.status_code, 200)
        lists = response.json["body"]
        items = lists["items"]
        self.assertEqual(len(items), 1)
        client.delete("/lists/A-list/item/0")
        response = client.get("/lists/A-list")
        self.assertEqual(response.status_code, 200)
        lists = response.json["body"]
        items = lists["items"]
        self.assertEqual(len(items), 0)

    def test_delete_list(self):
        client = app.test_client()
        client.post("/lists", json={"name": "A list"})
        response = client.get("/lists")
        lists = response.json["body"]
        self.assertEqual(len(lists), 1)
        client.delete("/lists/A-list")

        response = client.get("/lists")
        lists = response.json["body"]
        self.assertEqual(len(lists), 0)
