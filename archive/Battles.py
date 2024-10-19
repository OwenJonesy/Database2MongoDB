import pymongo
import csv

# Read battles data
battles_file = 'battles.csv'
with open(battles_file, 'r') as file:
    battles_data = list(csv.DictReader(file))

# Modify attacker and defender names
for battle in battles_data:
    attackers = [f"House {battle[attacker]}" for attacker in ['attacker_1', 'attacker_2', 'attacker_3', 'attacker_4'] if battle[attacker]]
    defenders = [f"House {battle[defender]}" for defender in ['defender_1', 'defender_2', 'defender_3', 'defender_4'] if battle[defender]]

    battle['attacker_1'] = attackers[0] if attackers else None
    battle['attacker_2'] = attackers[1] if len(attackers) > 1 else None
    battle['attacker_3'] = attackers[2] if len(attackers) > 2 else None
    battle['attacker_4'] = attackers[3] if len(attackers) > 3 else None

    battle['defender_1'] = defenders[0] if defenders else None
    battle['defender_2'] = defenders[1] if len(defenders) > 1 else None
    battle['defender_3'] = defenders[2] if len(defenders) > 2 else None
    battle['defender_4'] = defenders[3] if len(defenders) > 3 else None

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the GameOfThrones database
db = client["GameOfThrones"]

# Select or create the Battles collection
battles_collection = db["Battles"]

# Insert data into the Battles collection
battles_collection.insert_many(battles_data)

# Close the MongoDB connection
client.close()
