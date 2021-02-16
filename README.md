# poetry-demo

An example project used to explain the most important features of Poetry. In this example, we build an API for managing TODO lists.


## Run
```
docker build -t todo . 
docker run -it -p 5000:5000 todo
```

## Test

```
docker build -t todo . 
docker run todo python -m unittest
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
curl -X DELETE http://localhost:5000/lists/My-todo-list/0

# Delete the complete list
curl -X DELETE http://localhost:5000/lists/My-todo-list
```
=======
An example project used to explain the most important features of Poetry

## Windows
How to run on windows:
0.  For the bellow commands I use powershell. CMD should work as well but is not recommended.
1.  Make sure python3.9 or higher is installed on your machine. (https://www.python.org/downloads/)
2.  Prepare your environment by running ```.\prep_win_env.ps1``` 
    It will install Poetry on your system, together with a windows wrapper to make a virtual environment.
    Poetry will also be installed in that virtual environment.
3.  You have now entered a virtual environment provisioned with the Poetry dependencies needed for you project.
4.  You can add or remove dependencies by running ```poetry add <packagename>``` or ```poetry remove <packagename>``` .
5.  Poetry will resolve dependencies for you while also preventing package conflicts.
6.  To reload your environment after you added/removed dependencies first run ```deactivate``` , remove the "venv" folder and then run step 2 again.
7.  Included in this project is a small API that shows a working application - it will use the dependencies managed by poetry. 
    Execute the file to see it's output. (It needs valid AWS creds)

