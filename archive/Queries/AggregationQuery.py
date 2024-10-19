import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Specify a condition for the aggregation pipeline (e.g., houses with more than 3 battles)
pipeline = [
    {"$match": {"Battles": {"$exists": True, "$not": {"$size": 0}}}},
    {"$addFields": {"NumBattles": {"$size": {"$ifNull": ["$Battles", []]}}}},
    {"$match": {"NumBattles": {"$gt": 3}}}
]

# Aggregation query to select houses with more than 3 battles
aggregation_query = houses_collection.aggregate(pipeline)

# Print houses that meet the aggregation criteria in JSON format
for house in aggregation_query:
    print(house)

# Close the MongoDB connection
client.close()
