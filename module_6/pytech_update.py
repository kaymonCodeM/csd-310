'''
This program will connect to mongodb database and return the new updated lastname to Fred

Kaymon McCain
Assignment 6.2
4/17/2021
'''
import pymongo
from pymongo import MongoClient

# Connect and retrive the students collection
url = "mongodb+srv://admin:admin@cluster0.f2jka.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["pytech"]
collection = db["students"]

# print out all the documents within the student collection
students = collection.find({})
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    student_id = student["student_id"]
    student_first_name = student["first_name"]
    student_last_name = student["last_name"]
    print(f"Student ID: {student_id}")
    print(f"First Name: {student_first_name}")
    print(f"Last Name: {student_last_name}")
    print()

# Update Fred document last_name to Smith
collection.update_one(
    {"student_id": 1007}, {"$set": {"last_name": "Smith"}})

# Print out Fed new last name
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
docFred = collection.find_one({"student_id": 1007})
student_id = docFred["student_id"]
student_first_name = docFred["first_name"]
student_last_name = docFred["last_name"]
print(f"Student ID: {student_id}")
print(f"First Name: {student_first_name}")
print(f"Last Name: {student_last_name}")
print()

# Update Fed document last_name back to Morris
collection.update_one(
    {"student_id": 1007}, {"$set": {"last_name": "Morris"}})
