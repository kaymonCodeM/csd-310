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
docKaymon = collection.find_one({"student_id": 1009})
kaymon_student_id = docKaymon["student_id"]
kaymon_student_first_name = docKaymon["first_name"]
kaymon_student_last_name = docKaymon["last_name"]
print(f"Student ID: {kaymon_student_id}")
print(f"First Name: {kaymon_student_first_name}")
print(f"Last Name: {kaymon_student_last_name}")
print()
