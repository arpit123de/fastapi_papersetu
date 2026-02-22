from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI")) # connection string
db = client["papersetu"] # database name
agent_collection = db["agents"]# collection name / table
customer_collection = db["customer"] # collection / table name
newspaper_collection = db["newspaper"] # collection / table for newspaper
subsciption_collection = db["subscription"] # collection / table for subscription of customer