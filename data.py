import json
import os

FILE = "expenses.json"

def load():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []

def save(e):
    with open(FILE, "w") as file:
        json.dump(e, file, indent=4)