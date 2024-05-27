"""
In this assignment we will create a Flask interface for ingesting data.
As we haven't discussed different storage systems, in this assignment your program should just keep the data in memory. 
That is, store it in a fitting data structure: list, dictionary - whichever fits your use case best.

We will use the classic book store example here. We have 3 routes: 
1st - that the end-user uses to sell books into the store; 
2nd - to list the book inventory;
3rd - that the end-user can use to purchase books from the store.

1) Implement the route: /sell/

This route is accessed via POST method. The data is delivered in a JSON.
When the interface gets a "sell request", it should insert the item into the inventory. 
The items should have the following information: Title, Author, Year of Publication.
An id is associated with each individual book by the program. 
This id is shown in the response from the /list/ route and it is referenced by the /purchase/ route.

2) Implement the route: /list/

This route is accessed via GET method only. 
It returns a list of the items currently in the inventory, showing their index and the information.

3) Implement the route: /purchase/<item id>/

This route is accessed via GET method. 
The route checks if the item referenced by the <item id> is in the inventory. 
If the item is in the inventory it is removed from there and an 'OK'-response is sent to the client. 
If there are no items with <item id> in the inventory a 'Not found'-response is sent to the client.

4) Implement a separate Python script to generate books into the book store. 
You can use the following code snippet as a starting point.

import requests

rreply = requests.post('http://localhost:5000/sell/', json={"title": "book","author":"Esteri","year_of_publication":1990})
print(rreply.status_code)
print(rreply.json())

Think of a way to randomize some of the input data, 
so that you can use the script to feed 100 books into the book store easily, without need to write 100 JSONs manually.
"""

import flask
from flask import request, jsonify

inventory = {}          # our data is stored in memory

# 1. route: /sell/
app = flask.Flask(__name__)
@app.route('/sell/', methods=['POST'])
def api_request_sell():
    global inventory
    print(request.json)
    data = request.json
    inventory[len(inventory) + 1] = {"title": request.json["title"], "author": request.json["author"], "year_of_publication": int(request.json["year_of_publication"])}
    return f"Your request: {str(data)}\n"

# 2. route: /list/
@app.route('/list/', methods=['GET'])
def api_request_list():
    global inventory
    #return f"Available books: {str(inventory)}\n"
    return jsonify(inventory)       # Available books in the store as .json

# 3. route: /purchase/<item id>/
@app.route('/purchase/<item_id>/', methods=['GET'])
def api_request_purchase(item_id):
    global inventory
    if int(item_id) not in inventory.keys():
        return "Not found\n"
    else:
        del inventory[int(item_id)]
        return "OK\n"

if __name__ == '__main__':
    app.run()