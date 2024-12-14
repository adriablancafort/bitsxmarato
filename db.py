from pymongo import MongoClient
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        load_dotenv()

        mongo_ip = os.getenv("MONGO_IP")
        mongo_port = int(os.getenv("MONGO_PORT"))
        mongo_user = os.getenv("MONGO_USER")
        mongo_password = os.getenv("MONGO_PASSWORD")
        mongo_db_name = os.getenv("MONGO_DB_NAME")

        mongo_url = f"mongodb://{mongo_user}:{mongo_password}@{mongo_ip}:{mongo_port}"

        try:
            self.client = MongoClient(mongo_url)
            self.db = self.client[mongo_db_name]
            print("Connection successful.")
        except Exception as e:
            print("Connection failed:", e)
            self.client = None
            self.db = None

    def get_collection(self, collection_name):
        if self.db:
            return self.db[collection_name]
        else:
            raise Exception("Database connection is not established.")
