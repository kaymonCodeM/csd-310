'''
Kaymon McCain
Assignment 5.2
4/11/2021
'''
import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.f2jka.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["pytech"]
collectionNames = db.list_collection_names()
print(collectionNames)
