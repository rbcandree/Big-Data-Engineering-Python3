from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017, username = 'your_username', password = 'your_password')

#db = client["your_db_name"]
db = client.your_db_name

#collection = db["books"]
collection = db.books

# 'Pretty print' of the result of .find_one() function on 'books' collection
pprint.pprint(collection.find_one({'_id': 1}))