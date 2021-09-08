import requests


def insert_data():
    for port in [5000, 5001, 5002]:
        host = f"http://localhost:{port}"
        print(f"Inserting data at {host}")

        requests.post(f"{host}/lists", json={"name": "Monday"}).raise_for_status()
        requests.post(
            f"{host}/lists/Monday/item",
            json={"name": "Shopping", "description": "Buy some food for the week"},
        ).raise_for_status()
        requests.post(
            f"{host}/lists/Monday/item",
            json={"name": "Cleaning", "description": "The kitchen is really gross"},
        ).raise_for_status()

        requests.get(f"{host}/lists").raise_for_status()
        requests.get(f"{host}/lists/Monday").raise_for_status()

        requests.post(f"{host}/lists", json={"name": "test-list"}).raise_for_status()
        requests.post(
            f"{host}/lists/test-list/item",
            json={"name": "test-item", "description": "test item"},
        ).raise_for_status()
        requests.delete(f"{host}/lists/test-list/item/test-item").raise_for_status()
        requests.delete(f"{host}/lists/test-list").raise_for_status()


insert_data()
