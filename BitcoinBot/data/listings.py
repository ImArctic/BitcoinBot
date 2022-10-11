from tinydb import TinyDB, Query
import json
listings_db = TinyDB("data/listings.json")
listings = listings_db.table("listings")

def format():
   with open("data/listings.json", "r") as rf:
      data = json.load(rf)
   with open("data/listings.json", "w") as wf:
      json.dump(data, wf, indent=4)

def getlisting(id):
    return listings.search(Query().id == id)[0]

def getProduct(id):
    listing_data = listings.search(Query().id == id)[0]
    products = listing_data["products"]
    soldProduct = products.pop()
    listing_data["products"] = products
    listings.update(listing_data)
    format()
    return soldProduct



