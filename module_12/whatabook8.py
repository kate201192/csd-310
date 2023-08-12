import sys
import mysql.connector
from mysql.connector import errorcode


#connecting to database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
}

#main menu for user 

def show_menu():
    print("---Main Menu---")

    print("1. View Books")
    print("2. Store Locations")
    print("3. Account")
    print("4. Close Program")

    try:
        choice = int(input('  <-Input Here'))

        return choice
    except ValueError:
        print("invalid option, goodbye")

        sys.exit(0)

#select query to view all books 

def show_all_books(_cursor):
    _cursor.execute("select book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("Book Listings")

    for book in books:
        print("Book Name: {}\n Author{}\n Details{}\n".format(book[0],book[1],book[2]))

    sys.exit(0)
#select query to view location         
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Locale: {}\n".format(location[1]))
    sys.exit(0)

#validate user 
def show_user():

    try:
        user_id = int(input('  <-Input Here'))

        if user_id < 0 or user_id > 3:
            print("invalid option, goodbye")
            sys.exit(0)

        return user_id
    
    except ValueError:
        print("invalid option, goodbye")

    sys.exit(0)

#account menu

def show_account():

    try:
        print("---Customer Menu---")
        print("1. Wishlists")
        print("2. Add a book")
        print("3. Return to main menu")

        account_option = int(input('  <-Input Here'))

        return account_option

    except ValueError:
        print("invalid option, goodbye")

    sys.exit(0)

#inner join to query wishlist items 

def show_wishlist(_cursor, User_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(User_id))
    
    wishlist = _cursor.fetchall()

    print("Wishlist Items")

    for book in wishlist:
        print("Book {} \n Author {}".format(book[4],book[5]))

        def show_book_options(_cursor, User_id):

            look_up = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(User_id))

            print(look_up)

            _cursor.execute(look_up)

            books_to_add = _cursor.fetchall()

            print("All books")

            for book in books_to_add:
                print(" Book ID: {} \n Book Name:{}".format(book[0],book[1]))

        def add_to_wishlist(_cursor, User_id, Book_id):

            _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(User_id, Book_id))
            
        sys.exit(0)
try:

        db = mysql.connector.connect(**config)

        myCursor = db.cursor()

        print("Welcome to What A Book App")

        selection = show_menu ()

        while selection != 4:

            if selection == 1:
                show_all_books(myCursor)

            if selection == 2:
                show_locations(myCursor)

            if selection == 3:
                User_id = show_user()
                account_option = show_account()

                while account_option != 3:
                    if account_option == 1:
                        show_wishlist(myCursor, User_id)  

                    if account_option != 2:
                            show_book_options(myCursor, User_id)

                            book_id = int(input("     <-enter id of book to add"))

                            add_to_wishlist(_cursor, User_id, book_id)

                            db.commit()

                            print("added to wishlist")

                    if selection < 0 or selection > 3:
                            print("There has been an error, please try again")

                    user_selection = show_menu()

                print("the program has ended")
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()

                    
                    

            





