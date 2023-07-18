from flask import Flask
from pymongo import MongoClient
from flask import Flask, request

from bson.objectid import ObjectId

        
app = Flask(__name__)
client = MongoClient("mongodb+srv://faizanmd:faizan123@cluster0.defifv6.mongodb.net/mohsindb?retryWrites=true&w=majority")
db = client["mohsindb"]

@app.route("/")
def home():
    return "Welcome to Python Projects"



class User: # also this will be diffrent according to the project
    def __init__(self, name, email):
        self._id = ObjectId()
        self.name = name
        self.email = email

def add_user(user_data):
    users_collection = db["users"]  #   new collection will be there according to the project
    user = User(user_data["name"], user_data["email"])
    user_data = {           # data wil be diffrent
        "_id": user._id, 
        "name": user.name,
        "email": user.email
    }
    users_collection.insert_one(user_data)

@app.route("/create", methods=["POST"])
def create_user():
    user_data = request.get_json()
    add_user(user_data)

    return "User created successfully!"

#-----------------------------------------------------------------


if __name__ == "__main__":
    app.run()

