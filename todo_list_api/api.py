import json

from flask import Flask, request

from todo_list_api.controller import TodoListController
from todo_list_api.exceptions import HTTPException

app = Flask(__name__)


@app.errorhandler(HTTPException)
def handle_error(error):
    return {"statusCode": error.status_code, "body": error.reason}


controller = TodoListController()


@app.route("/")
def landing_page():
    return {"statusCode": 200, "body": "Hello, welcome to the Todo list app!"}


@app.route("/lists", methods=["GET"])
def get_lists():
    lists = controller.get_lists()
    return {"statusCode": 200, "body": [list_.dict() for list_ in lists]}


@app.route("/lists", methods=["POST"])
def create_list():
    data = json.loads(request.data.decode("utf-8"))
    controller.create_list(data["name"], [])
    return {"statusCode": 200, "body": "Created"}


@app.route("/lists/<list_name>", methods=["GET"])
def get_list(list_name: str):
    return {"statusCode": 200, "body": controller.get_list(list_name).dict()}


@app.route("/lists/<list_name>", methods=["DELETE"])
def delete_list(list_name: str):
    controller.delete_list(list_name)
    return {"statusCode": 200, "body": "Deleted"}


@app.route("/lists/<list_name>", methods=["POST"])
def add_item(list_name):
    data = json.loads(request.data.decode("utf-8"))
    controller.add_item(list_name, data["name"], data["description"])
    return {"statusCode": 200, "body": "Added"}


@app.route("/lists/<list_name>/<index>", methods=["DELETE"])
def delete_item(list_name, index):
    controller.delete_item(list_name, int(index))
    return {"statusCode": 200, "body": "Deleted"}


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
