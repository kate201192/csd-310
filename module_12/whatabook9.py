#Katherine Burman
#CYBR 410 Final Submission 
#Prof Haas



#adding pieces to ensure sql connects to the file
import sys
import mysql.connector
from mysql.connector import errorcode

#configuring information for the database to be accessed and authenticated
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#defining the menu the user will see when opening the application 
def show_menu():
    print("\n  -- Main Menu --")

    print("    1. View Books\n    2. View Stores \n    3. View Account\n    4. Exit ")

#error handling for options not on the list 
    try:
        choice = int(input('Input Option Here:'))

        return choice
    except ValueError:
        print(" there has been an error goodbye ")

        sys.exit(0)

#defining the method to select and return the books listed within the database using itteration to return back
def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("Book")
    
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2]))

    
#defining the method to select and itterate over stores to show locations to the user 
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    locations = _cursor.fetchall()

    print("Store Locations")
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

#defining user ids to allow as input for option 3 
def authenticate_user():

    try:
        user_id = int(input('Input User ID: '))

        if user_id < 0 or user_id > 3:
            print("there has been an error goodbye")
            sys.exit(0)

        return user_id
    except ValueError:
        print("there has been an error goodbye")

        sys.exit(0)

#defining the method for the menu for option 3 
def show_account_menu():
    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add A Book\n        3. Main Menu")
        account_option = int(input('Input Option Here:'))

        return account_option
    except ValueError:
        print("there has been an error goodbye ")

        sys.exit(0)

#defining the method to return back the wishlist items by joining the tables for the inner join query 
def show_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("Current Wishlist Items ")

    for book_id in wishlist:
        print("Book Name: {}\n Author: {}\n".format(book_id[0], book_id[1]))  #after much trial and error still not getting the proper itterations to pull to present to the user 

# define query to show the available books to add to the wishlist using select query 
def show_books_to_add(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("Available Books")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

#insert into query as method to add wishlist book to the users account 
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

#start the application and run parts together
try:

    db = mysql.connector.connect(**config) 

    cursor = db.cursor() 

    print("Welcome to What a book :) ")

#calling  method to show the menu 

    user_selection = show_menu() 
    
    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = authenticate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:

                    show_books_to_add(cursor, my_user_id)

                    book_id = int(input("Enter Book Id Here:"))
                    
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    db.commit() 

                    print("Book{} was added to your wishlist".format(book_id))

                if account_option < 0 or account_option > 3:
                    print("this account does not exist")

                account_option = show_account_menu()
        
        if user_selection < 0 or user_selection > 4:
            print("This user does not exist")
            
        user_selection = show_menu()

    print("GOODBYE")

except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("There is an authentication error")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("There is a database error")

    else:
        print(err)

finally:

    db.close()