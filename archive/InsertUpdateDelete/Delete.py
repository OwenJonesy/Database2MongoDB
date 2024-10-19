import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Delete a document from the "Houses" collection
query = {"Name": "House New"}

result = houses_collection.delete_one(query)
print(f"Deleted {result.deleted_count} document(s)")

# Close the MongoDB connection
client.close()
