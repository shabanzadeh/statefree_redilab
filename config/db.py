from pymongo import MongoClient
db_connection = MongoClient("mongodb://localhost:27017")
db = db_connection.redilab
collection = db["users"]