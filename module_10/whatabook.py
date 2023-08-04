import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aliyah",
    database="whatabook"
    )

mycursor = db.cursor()

    #Rows 15,16,19, 21 show creation of tables 

#mycursor.execute("CREATE TABLE User (first_name VARCHAR(75) NOT NULL, last_name VARCHAR(75) NOT NULL, user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY )")

#mycursor.execute("CREATE TABLE Store (store_id INT NOT NULL PRIMARY KEY, locale VARCHAR(500) NOT NULL)")

#mycursor.execute("CREATE TABLE Book (book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, book_name VARCHAR(200) NOT NULL, details VARCHAR(500), author VARCHAR(200) NOT NULL)")

#mycursor.execute("CREATE TABLE Wishlist (wishlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL, book_id INT NOT NULL, FOREIGN KEY(user_id) REFERENCES User(user_id), FOREIGN KEY(book_id) REFERENCES Book(book_id)

    #Rows 25,27,29 show creation of users

#mycursor.execute("INSERT INTO User (first_name, last_name) VALUES ('matt', 'schiller')")

#mycursor.execute("INSERT INTO User (first_name, last_name) VALUES ('richard', 'feingold')")

#mycursor.execute("INSERT INTO User (first_name, last_name) VALUES ('george', 'baker')")


    #Rows 34,36,38 show creation of wishlist items 

#mycursor.execute("INSERT INTO Wishlist (user_id, book_id) VALUES ((SELECT user_id FROM user WHERE first_name = 'Matt'), (SELECT book_id FROM book WHERE book_name = 'Spare'))")

#mycursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES (SELECT user_id FROM user WHERE first_name = 'richard'),(SELECT book_id FROM book WHERE book_name = 'Light Bringer'));")

#mycursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES ( (SELECT user_id FROM user WHERE first_name = 'george'), (SELECT book_id FROM book WHERE book_name = 'Happy Place'));")

#db.commit




