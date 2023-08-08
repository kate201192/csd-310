import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user= "root",
    password= "aliyah",
    database= "whatabook",
    )

mycursor = db.cursor()

mycursor.execute("CREATE TABLE User (first_name VARCHAR(75) NOT NULL, last_name VARCHAR(75) NOT NULL, user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, )")

mycursor.execute("DESCRIBE User")

for x in mycursor:
    print(x)