from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch the Mongo URI from the environment variable
uri = os.getenv("MONGO_URI")
client = MongoClient(uri)
db = client["swift_planner"]  # Replace with your DB name
users_collection = db["users"]  # The collection where you will store user data

print("Connected to MongoDB!")


def insert_user_data(name, email, password):
    # Insert user data into the 'users' collection
    user = {
        "name": name,
        "email": email,
        "password": password  # Consider hashing the password in production
    }
    users_collection.insert_one(user)
