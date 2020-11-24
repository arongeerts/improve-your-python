# poetry-demo
An example project used to explain the most important features of Poetry. In this example, we build an API for managing TODO lists.

## Usage

These calls can be made using curl to test the api

```
# Create a new list
curl -X POST http://localhost:5000/lists -d '{"name":"example_list"}' -H "Content-Type:application/json"
# Add an item to a list
curl -X POST http://localhost:5000/lists/example_list -d '{"name":"task1","description":"The first task on the list!"}' -H "Content-Type:application/json"
# Get all the lists
curl http://localhost:5000/lists
# Get a specific list
curl http://localhost:5000/lists/example_list
# Delete an item from the list
curl -X DELETE http://localhost:5000/lists/example_list/0
# Delete the complete list
curl -X DELETE http://localhost:5000/lists/example_list
```
