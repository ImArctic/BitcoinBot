from tinydb import TinyDB, Query
import json

users_db = TinyDB("data/users.json")
users = users_db.table("users")

def format():
   with open("data/users.json", "r") as rf:
      data = json.load(rf)
   with open("data/users.json", "w") as wf:
      json.dump(data, wf, indent=4)

def getUser(id):
    return users.search(Query().id == id)[0]

def addBalance(id, amount):
    User = users.search(Query().id == id)[0]
    User["balance"] += round(amount, 2)
    users.update(User)
    format()

