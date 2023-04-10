import json
from pymongo import MongoClient
import pprint

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

# Load database
load(coll, "data.json.codechallenge.janv22.RHOBS.json")

# Count the number of men and women
print("Nombre de femmes:", coll.count_documents({"sex": "F"}))
print("Nombre d'hommes:", coll.count_documents({"sex": "M"}))


# Get company by the number of employees
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

print("\n\nGet companies by number of employees\n")
print(get_company_number_employees(coll, 50))

def age_pyramid(collection):
    pyramid = collection.aggregate([
        { "$addFields": {
            "birthdate": {
                "$toDate": "$birthdate"
            }} 
        },
        { "$addFields":
            { "age": { "$dateDiff": { "startDate": "$birthdate", "endDate": "$$NOW", "unit": "year" } } }
        },
        { "$bucket":
            {
                "groupBy" : "$age", 
                "boundaries":[0,10,20,30,40,50,60,70,80,90,100], 
                "default":"other", 
                "output" : 
                    {
                        "total" : {"$sum" : 1}, 
                    }
            }
        }
    ])
    return list(pyramid)

print("\n\nAge Pyramid \n")
print(age_pyramid(coll))