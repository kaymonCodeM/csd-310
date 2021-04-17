'''
This program will insert and delete a new document Sawyer student_id 1010
https://github.com/kaymonCodeM/csd-310.git

Kaymon McCain
Assignment 6.3
4/17/2021
'''
import pymongo
from pymongo import MongoClient

# Connect and retrive the students collection
url = "mongodb+srv://admin:admin@cluster0.f2jka.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client["pytech"]
collection = db["students"]

students = collection.find({})

# Print out the starting collection
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    student_id = student["student_id"]
    student_first_name = student["first_name"]
    student_last_name = student["last_name"]
    print(f"Student ID: {student_id}")
    print(f"First Name: {student_first_name}")
    print(f"Last Name: {student_last_name}")
    print()

# Insert new student document Sawyer
sawyer = {"student_id": 1010, "first_name": "Sawyer", "last_name": "Johnson"}

print("-- INSERT STATEMENT --")
sawyer_student_id = collection.insert_one(sawyer).inserted_id
print(
    f"Inserted Student Record Fred Morris into the students collection with document id {sawyer_student_id}")

# display the new inserted student Sawyer
print("\n-- DISPLAYING STUDENT TEST DOC --")
docSawyer = collection.find_one({"student_id": 1010})
sawyer_student_id = docSawyer["student_id"]
sawyer_student_first_name = docSawyer["first_name"]
sawyer_student_last_name = docSawyer["last_name"]
print(f"Student ID: {sawyer_student_id}")
print(f"First Name: {sawyer_student_first_name}")
print(f"Last Name: {sawyer_student_last_name}")
print()

# Delete Sawyer document
collection.delete_one({"student_id": 1010})

students = collection.find({})
# diplay collection after deleting Sawyer document
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    student_id = student["student_id"]
    student_first_name = student["first_name"]
    student_last_name = student["last_name"]
    print(f"Student ID: {student_id}")
    print(f"First Name: {student_first_name}")
    print(f"Last Name: {student_last_name}")
    print()
