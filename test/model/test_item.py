from unittest import TestCase

from todo_list_api.model.item import Item


class TestItem(TestCase):
    example_item = Item(
        name="Water plants", description="Don't forget to water the plants"
    )

    def test_dict(self):
        expected = {
            "name": "Water plants",
            "description": "Don't forget to water the plants",
        }
        got = self.example_item.dict()
        self.assertEqual(expected, got)

    def test_json(self):
        expected = '{"name": "Water plants", "description": "Don\'t forget to water the plants"}'
        got = self.example_item.json()
        self.assertEqual(expected, got)

    def test_from_json(self):
        i = '{"name":"Water plants", "description": "Don\'t forget to water the plants"}'
        item = Item.from_json(i)
        self.assertEqual(self.example_item, item)
