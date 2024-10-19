import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Query to select all houses and sort them by gender in ascending order
sorted_houses_query = houses_collection.find().sort("Members.Male", pymongo.ASCENDING)

# Print all houses sorted by gender in JSON format
for house in sorted_houses_query:
    print(house)
