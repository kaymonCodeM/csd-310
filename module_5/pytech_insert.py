
'''
Kaymon McCain
Assignment 5.3
4/11/2021
'''
import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.f2jka.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["pytech"]
collection = db["students"]


fred = {"student_id": 1007, "first_name": "Fred", "last_name": "Morris"}
hannah = {"student_id": 1008, "first_name": "Hannah", "last_name": "Ashburn"}
kaymon = {"student_id": 1009, "first_name": "Kaymon", "last_name": "McCain"}

print("-- INSERT STATEMENT --")
fred_student_id = collection.insert_one(fred).inserted_id
print(
    f"Inserted Student Record Fred Morris into the students collection with document id {fred_student_id}")
hannah_student_id = collection.insert_one(hannah).inserted_id
print(
    f"Inserted Student Record Hannah Ashbur into the students collection with document id {hannah_student_id}")
kaymon_student_id = collection.insert_one(kaymon).inserted_id
print(
    f"Inserted Student Record Kaymon McCain into the students collection with document id {kaymon_student_id}")
