import pymongo
import json
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection
with open("/Users/youcefbaleh/Desktop/H3_Cours/NoSQL/cour-nosql/MongoDB/accounts.json", "r") as file:
    data = json.load(file)


result = collection.insert_many(data)

print("Inserted data with the following IDs:", result.inserted_ids)


