from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["StudyMaster"]
users = db["users"]

def insert_user(user_data):
    """Insert a new user into the database."""
    result = users.insert_one(user_data)
    print(f"Inserted user with ID: {result.inserted_id}")

def find_users(filter_query={}):
    """Find users based on a query."""
    return users.find(filter_query)

def update_user_schedule(user_name, schedule):
    """Update a user's schedule."""
    users.update_one({"name": user_name}, {"$set": {"schedule": schedule}})
