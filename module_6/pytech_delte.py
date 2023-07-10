from pymongo import MongoClient

connection_string ="mongodb+srv://admin:admin@cluster0.hj5iwow.mongodb.net/pytech"

client = MongoClient(connection_string)

#declaring my db 

db = client.get_database("pytech")

# get the students 
students = db.students

# find all students in the collection 
student_list = students.find({})

#to print all students in collection 
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "  First Name: " + doc["first_name"] + "  Last Name: " + doc["last_name"])

Larry = { 
    "first_name" : "Larry",
    "student_id" : "1010",
     "last_name" : "Spence",
    }

Larry_student_id = students.insert_one(Larry).inserted_id

#to print all students 
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "  First Name: " + doc["first_name"] + "  Last Name: " + doc["last_name"])


# attempt to validate new addition of larry 
tester = students.find_one({"student_id": "1010"})
print(tester)

# remove larry 
deleted_tester = db.students.delete_many({"student_id": "1010"})

#to print all students again  
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "  First Name: " + doc["first_name"] + "  Last Name: " + doc["last_name"])
