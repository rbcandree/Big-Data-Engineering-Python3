from flask import Flask, request, jsonify
from pymongo import MongoClient 
  
app = Flask(__name__) 
  
# Set up MongoDB connection and access collection
client = MongoClient('mongodb://localhost:27017/', username = 'your_username', password = 'your_password') 
  
# access database 'your_db_name' 
db = client['your_db_name'] 
  
# access collection 'books' 
collection = db['books'] 
  
# Add data to MongoDB route 
@app.route('/add_data/', methods=['POST']) 
def add_data(): 
    data = request.json
    
    # Insert documents into MongoDB
    collection.insert_one(data) 
    return 'Data has been added to MongoDB'

# Get data from MongoDB route 
@app.route('/get_data/', methods=['GET']) 
def get_data():
    
    # All documents as .json
    documents = list(collection.find())
    return jsonify(documents)

if __name__ == '__main__': 
    app.run() 