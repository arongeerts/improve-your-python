# Improving your Python skills

This project is used as a demo going along with a presentation on how to take your Python skills to the next level.
It is meant for people that already have some Python experience, but are unaware of some best practices and patterns, 
that may improve the quality of their code.

In this example, we build an API for managing TODO lists.

## What it is

This project consists of a TODO-list API with a built-int plugin system. The plugin system allows you to change the 
database backend that is used in the project, without having to change code. 
All you have to do is install the plugin as a package and 
set an environment variable to indicate which backend you want to use.

3 Backends are available for the underlying database:
* An in-memory key-value store
* A MySQL database
* A DynamoDB table

With these different backends, we want to show design patterns for interfacing and 
a pattern to dynamically import classes to allow interchangeable modules.

## The docker-compose file

The project can be ran locally using the `docker-compose.yml` file in the project root. 
This compose file will spin up 5 containers.

* The API with in-memory database at http://localhost:5000
* The API with MySQL database at http://localhost:5001
* The API with DynamoDB database at http://localhost:5002
* A MySQL database 
* Localstack with DynamoDB enabled

You can then run
```
docker-compose up
```
to set up the full stack.

## Plugin system

We use a plugin system to demonstrate the 
[Interface design pattern](http://best-practice-software-engineering.ifs.tuwien.ac.at/patterns/interface.html).
The goal of this pattern is to allow flexible implementation of a static contract between two modules. 
In this case, the modules are the database and the application controller. 
The database implementation is abstracted away using an Abstract Base Class (ABC). 
The API will then dynamically import the correct implementing class based 
on the `TODO_LIST_DB_IMPLEMENTATION` environment variable, which is a reference to the class that is intended as DB.

We want to show here that the controller does not care about what the backend is, 
all it needs is to respect the contract that is defined by the Database interface.

These types of implementations allow for flexible evolution of systems. 
Thinking about interfaces first, rather than implementations, forces us to thing more conceptually 
and removes the focus from technology-specific details.

## Test

```
python -m unittest
```

## Usage

These calls can be made using curl to test the api

```
# Create a new list
curl -X POST http://localhost:5000/lists -d '{"name":"My todo list"}' -H "Content-Type:application/json"

# Add an item to a list
curl -X POST http://localhost:5000/lists/My-todo-list -d '{"name":"task1","description":"The first task on the list!"}' -H "Content-Type:application/json"

# Get all the lists
curl http://localhost:5000/lists

# Get a specific list
curl http://localhost:5000/lists/My-todo-list

# Delete an item from the list
curl -X DELETE http://localhost:5000/lists/My-todo-list/task1

# Delete the complete list
curl -X DELETE http://localhost:5000/lists/My-todo-list
```

There is also a script included `scripts/insert_data.py` to insert some dummy data in all API's
