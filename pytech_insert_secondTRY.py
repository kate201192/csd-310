from pymongo import MongoClient

connection_string ="mongodb+srv://admin:admin@cluster0.hj5iwow.mongodb.net/pytech"

client = MongoClient(connection_string)

db = client.get_database("pytech")

my_collection = db.get_collection('students')

Larry = { 
    "name" : "Larry",
    "student_ID" : "1009",
    }

Larry_student_id = my_collection.insert_one(Larry).inserted_id


Lisa = { 
    "name" : "Lisa",
    "student_ID" : "1007",
    }

Lisa_student_id = my_collection.insert_one(Lisa).inserted_id


Logan = { 
    "name" : "Logan",
    "student_ID" : "1008",
    }

Logan_student_id = my_collection.insert_one(Logan).inserted_id

print(Larry_student_id)
print(Logan_student_id)
print(Lisa_student_id)

print(my_collection.student_id)