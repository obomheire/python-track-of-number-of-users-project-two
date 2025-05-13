import os

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient(os.getenv("MONGO_DATABASE_URL"))
db = client.track_user_no_db
UserNum = db["number_of_users"]

UserNum.insert_one({"users_number": 0})


class Visit(Resource):
    def get(self):
        prev_num = UserNum.find_one({})["users_number"]
        new_num = prev_num + 1
        UserNum.update_one({}, {"$set": {"users_number": new_num}})
        return str("Hello user " + str(new_num))


api.add_resource(Visit, "/hello")

@app.route("/")
def hello_world():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(debug=True)
