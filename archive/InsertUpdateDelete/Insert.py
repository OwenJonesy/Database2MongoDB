import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Insert a new document into the "Houses" collection
new_house = {
    "Name": "House New",
    "Members": [
        {
            "Name": "New Member 1",
            "Male": 1,
            "Title": "Lord",
            "DateOfBirth": "2000-01-01",
            "Allegiances": ["House New"]
        }
    ],
    "Allies": ["Other House 1", "Other House 2"],
    "Battles": [
        {
            "Name": "Battle 1",
            "Year": 300,
            "AttackerKing": "Some King",
            "DefenderKing": "Another King",
            "Location": "Some Location",
            "Region": "Some Region"
        }
    ]
}

result = houses_collection.insert_one(new_house)
print(f"Inserted document ID: {result.inserted_id}")

# Close the MongoDB connection
client.close()
