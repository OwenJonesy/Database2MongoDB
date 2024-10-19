import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Update a document in the "Houses" collection
query = {"Name": "House New"}
update = {
    "$set": {
        "Members.0.Title": "Lord Paramount",
        "Allies": ["Updated Ally 1", "Updated Ally 2"],
        "Battles.0.Location": "Updated Location"
    }
}

result = houses_collection.update_one(query, update)
print(f"Modified {result.modified_count} document(s)")

# Close the MongoDB connection
client.close()
