from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
collection = db.mycollection

document = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
result = collection.insert_one(document)
print("Inserted document ID:", result.inserted_id)