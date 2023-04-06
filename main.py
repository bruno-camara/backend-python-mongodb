import json
from pymongo import MongoClient

def collection(uri):
    client = MongoClient(uri)
    database = client["rhobs"]
    collection = database["people"]
    return collection

def load(uri="localhost", datapath="data.json"):
    coll = collection(uri=uri)
    with open(datapath, "r") as fp:
        data = json.load(fp)

        for person in data:
            coll.insert_one(person)


load("localhost", "data.json.codechallenge.janv22.RHOBS.json")