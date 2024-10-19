import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Create a new collection named "Houses"
houses_collection = db["Houses"]

# Iterate through characters to update the "Houses" collection with members and allies
for character in db["Characters"].find():
    house_name = character.get("house")
    allegiances = character.get("Allegiances")
    if house_name:
        # Update or insert the house with a "Members" array
        houses_collection.update_one(
            {"Name": house_name},
            {"$push": {"Members": {
                "Name": character.get("name"),
                "Male": character.get("male"),
                "Title": character.get("title"),
                "DateOfBirth": character.get("dateOfBirth"),
                "Allegiances": allegiances
            }}},
            upsert=True
        )

        # Update allies based on allegiances, excluding "None"
        if allegiances and "None" not in allegiances:
            houses_collection.update_one(
                {"Name": house_name},
                {"$addToSet": {"Allies": allegiances}},
                upsert=True
            )

# Iterate through battles to update the "Houses" collection with battles
for battle in db["Battles"].find():
    # Update attacker houses
    for attacker in ["attacker_1", "attacker_2", "attacker_3", "attacker_4"]:
        attacker_house = battle.get(attacker)
        if attacker_house:
            # Update or insert battle information into the attacker's house
            houses_collection.update_one(
                {"Name": attacker_house},
                {"$push": {"Battles": {
                    "Name": battle["name"],
                    "Year": battle["year"],
                    "AttackerKing": battle["attacker_king"],
                    "DefenderKing": battle["defender_king"],
                    "Location": battle["location"],
                    "Region": battle["region"]
                }}},
                upsert=True
            )

    # Update defender houses
    for defender in ["defender_1", "defender_2", "defender_3", "defender_4"]:
        defender_house = battle.get(defender)
        if defender_house:
            # Update or insert battle information into the defender's house
            houses_collection.update_one(
                {"Name": defender_house},
                {"$push": {"Battles": {
                    "Name": battle["name"],
                    "Year": battle["year"],
                    "AttackerKing": battle["attacker_king"],
                    "DefenderKing": battle["defender_king"],
                    "Location": battle["location"],
                    "Region": battle["region"]
                }}},
                upsert=True
            )

# Close the MongoDB connection
client.close()
