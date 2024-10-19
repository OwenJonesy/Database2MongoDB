import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select the Houses collection
houses_collection = db["Houses"]

# Specify the house name for which you want to retrieve specific fields
target_house_name = "House Stark"

# Query to select specific fields (e.g., Name and Allies) of a specific house
house_projection_query = houses_collection.find(
    {"Name": target_house_name},
    {"Name": 1, "Allies": 1, "_id": 0}
)

# Print the projected fields of the specified house in JSON format
for result in house_projection_query:
    print(result)
