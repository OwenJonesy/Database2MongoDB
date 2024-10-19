import pymongo
import csv

# Read character predictions data
predictions_file = 'character-predictions.csv'
with open(predictions_file, 'r') as file:
    predictions_data = list(csv.DictReader(file))

# Read character deaths data
deaths_file = 'character-deaths.csv'
with open(deaths_file, 'r') as file:
    deaths_data = list(csv.DictReader(file))

# Combine data
combined_data = []
for prediction in predictions_data:
    name = prediction['name']
    death_entry = next((death for death in deaths_data if death['Name'] == name), None)

    if death_entry:
        combined_entry = {**prediction, **death_entry}
        combined_data.append(combined_entry)

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the gameofthrones database
db = client["GameOfThrones"]
# Select the characters collection
collection = db["Characters"]

# Insert data into MongoDB
collection.insert_many(combined_data)

# Close the MongoDB connection
client.close()
