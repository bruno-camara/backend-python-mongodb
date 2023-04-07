import json
from pymongo import MongoClient

def collection(uri):
    client = MongoClient(uri, 27017) # client to the mongod instance
    database = client["rhobs"]
    collection = database["people"] # collection can be thought of as roughly the equivalent of a table in a relational database
    return collection

def load(uri="localhost", datapath="data.json"):
    coll = collection(uri=uri)
    with open(datapath, "r") as fp:
        data = json.load(fp)

        for person in data:
            coll.insert_one(person)


load("mongodb://localhost:27017/", "data.json.codechallenge.janv22.RHOBS.json")