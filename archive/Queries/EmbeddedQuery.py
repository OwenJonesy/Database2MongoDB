import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Specify the house name for which you want to retrieve members
target_house_name = "House Stark"

# Query to select members of a specific house
house_members_query = houses_collection.find(
    {"Name": target_house_name},
    {"Members": 1, "_id": 0}
)

# Print members of the specified house in JSON format
for result in house_members_query:
    print(result)
