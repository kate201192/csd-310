#import statement

from pymongo import MongoClient

#connecting to my mongoDB students collections in lines 5-11

connection_string ="mongodb+srv://admin:admin@cluster0.hj5iwow.mongodb.net/pytech"

client = MongoClient(connection_string)

db = client.get_database("pytech")

my_collection = db.get_collection('students')

#in line 15 calling the students collection to update student id 1007, the new first name should be "TEST"

db.students.update_one({"student_id" : "1007"},{"$set" : {"first_name" : "TEST"}})

#to watch results I am calling the query from the last assignment 

docs = db.students.find({})

#once all results are found I want to pull student ID 1007

result = my_collection.find_one({"student_id": "1007"})

#after finding the result print to the screen 

print("  Student ID: " + result ["student_id"] + result ["first_name"] + result ["last_name"])