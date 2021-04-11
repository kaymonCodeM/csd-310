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

print("-- DISPLAYING STUDENT DOCUMENT FROM find one() QUERY --")
docKaymon = db.collection_name.find_one({"student_id": 1009})
student_id = student["student_id"]
student_first_name = student["first_name"]
student_last_name = student["last_name"]
print(f"Student ID: {student_id}")
print(f"First Name: {student_first_name}")
print(f"Last Name: {student_last_name}")
print()
