import pandas as pd
from pymongo import MongoClient
from pprint import PrettyPrinter

### Note: start mongodb with command 'mongod;
pp = PrettyPrinter(indent=2)
client = MongoClient(host="localhost", port=27017)

pp.pprint(list(client.list_databases()))

db = client["local"]

for c in db.list_collections():
    print(c["name"])

print("hello")
