import json
import traceback

from flask import Flask, request

from todo_list_api.app.controller import TodoListController
from todo_list_api.app.exceptions import HTTPException
from todo_list_api.db.interface import DataBase

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return {"statusCode": 404, "body": "Not Found"}, 404


@app.errorhandler(HTTPException)
def handle_error(error):
    return {"statusCode": error.status_code, "body": error.reason}, error.status_code


@app.errorhandler(500)
def handle_unknown_exception(error):
    traceback.print_exc()
    return {"statusCode": 500, "body": "Whoops, something went wrong!"}, 500


database = DataBase.initialize()  # The type will dynamically be chosen
controller = TodoListController(database)


@app.route("/")
def landing_page():
    return {
        "statusCode": 200,
        "body": f"Hello, welcome to the Todo list app! I am backed by {database.__class__.__name__}",
    }


@app.route("/lists", methods=["GET"])
def get_lists():
    lists = controller.get_lists()
    return {"statusCode": 200, "body": [list_.dict() for list_ in lists]}


@app.route("/lists", methods=["POST"])
def create_list():
    data = json.loads(request.data.decode("utf-8"))
    controller.create_list(data["name"])
    return {"statusCode": 200, "body": "Created"}


@app.route("/lists/<list_name>", methods=["GET"])
def get_list(list_name: str):
    return {"statusCode": 200, "body": controller.get_list(list_name).dict()}


@app.route("/lists/<list_name>", methods=["DELETE"])
def delete_list(list_name: str):
    controller.delete_list(list_name)
    return {"statusCode": 200, "body": "Deleted"}


@app.route("/lists/<list_name>/item", methods=["POST"])
def add_item(list_name):
    data = json.loads(request.data.decode("utf-8"))
    controller.add_item(list_name, data["name"], data["description"])
    return {"statusCode": 200, "body": "Added"}


@app.route("/lists/<list_name>/item/<item_name>", methods=["DELETE"])
def delete_item(list_name, item_name):
    controller.delete_item(list_name, item_name)
    return {"statusCode": 200, "body": "Deleted"}


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
