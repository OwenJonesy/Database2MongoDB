import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Query to select all documents in the Houses collection
all_houses_query = houses_collection.find()

# Print all documents in JSON format
for house in all_houses_query:
    print(house)
