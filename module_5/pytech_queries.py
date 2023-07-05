from pymongo import MongoClient

connection_string ="mongodb+srv://admin:admin@cluster0.hj5iwow.mongodb.net/pytech"

client = MongoClient(connection_string)

db = client.get_database("pytech")

my_collection = db.get_collection('students')

#to return all 

docs = db.students.find({})

for doc in docs:
    print(doc)

#to return one student id 

doc2 = db.collection_name.find_one({"student_id": "1007"})
 
print(doc2)


