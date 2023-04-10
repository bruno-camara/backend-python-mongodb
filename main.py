import json
from pymongo import MongoClient

def collection(uri):
    client = MongoClient(uri, 27017) # client to the mongod instance
    database = client["rhobs"]
    collection = database["people"] # collection can be thought of as roughly the equivalent of a table in a relational database
    return collection

def load(collection, datapath="data.json"):
    with open(datapath, "r") as fp:
        data = json.load(fp)

        for person in data:
            collection.insert_one(person)

# Create client, database and collection
coll = collection("mongodb://localhost:27017/")

# load database
load(coll, "data.json.codechallenge.janv22.RHOBS.json")

# Count the number of men and women
print("Nombre de femmes:", coll.count_documents({"sex": "F"}))
print("Nombre d'hommes:", coll.count_documents({"sex": "M"}))

def get_company_number_employees(collection, number_employees):
    companies = collection.aggregate([
        {
            "$group" : 
                {"_id" : "$company", 
                "num_employees" : {"$sum" : 1}
                }
        },
        {
            "$match" : {"num_employees" : {"$gt": number_employees}}
        }
    ])
    return list(companies)

print(get_company_number_employees(coll, 50))
