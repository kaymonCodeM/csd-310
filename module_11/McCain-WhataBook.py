'''
Kaymon McCain
Assignment 11.2
5/8/2021

https://github.com/kaymonCodeM/csd-310.git
'''
import sys
import mysql.connector
from mysql.connector import errorcode
from mysql.connector import IntegrityError

# This function will make a connection to mySQL database and return the connection


def connectSQL():
    mydb = mysql.connector.connect()
    try:
        config = {"host": "localhost", "user": "whatabook_user", "password": "MySQL8IsGreat!",
                  "database": "whatabook", "raise_on_warnings": True}
        mydb = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_KEYRING_ACCESS_DENIED_ERROR:
            print("    The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("    The specified database does not exist")
        else:
            print(err)
    finally:
        return mydb


# This function will show all the books within the watabook database
def showbooks(cursor):
    cursor.execute("SELECT book_id, book_name, detailsV, author FROM book;")
    books = cursor.fetchall()

    print("\nALL BOOKS!\n")
    for book in books:
        print("Book ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Details: {}".format(book[2]))
        print("Author: {}".format(book[3]))
        print()
    return

# This function will show all the locations within the watabook datbase


def show_locations(cursor):
    cursor.execute("SELECT store_id, locale FROM store;")
    stores = cursor.fetchall()

    print("\nSHOW STORE LOCATIONS\n")
    for store in stores:
        print("Store ID: {}".format(store[0]))
        print("Locale: {}".format(store[1]))
        print()
    return

# This function is the main menu of the program


def show_menu():

    userInput = ''
    try:
        print("\nMAIN MENU")
        userInput = input(
            "\nPlease enter one of the following:\n1 = View Books\n2 = View Store Locations\n3 = My Account\n4 = Exit\n")
    except ValueError:
        print("Please give valid input!")

    # View Book will show books
    if userInput == '1':
        db = connectSQL()
        cursor = db.cursor()
        showbooks(cursor)
        db.close()
    # View Store Locations will show store locations
    elif userInput == '2':
        db = connectSQL()
        cursor = db.cursor()
        show_locations(cursor)
        db.close()
    # My Account will return ma to proceed to account menu
    elif userInput == '3':
        return '3'
    # Back Input
    elif(userInput != '4'):
        print("INVALID ENTRY")
    # Return exit
    return userInput

# This function will show all the books that are not in the users wishlist


def show_books_to_add(cursor, user_id):
    booksToAdd = (
        "SELECT book_id, book_name, detailsV, author FROM book Where book_id NOT IN (SELECT book_id FROM wishlist where user_id = {});".format(user_id))
    cursor.execute(booksToAdd)
    books = cursor.fetchall()

    print("\nBOOKS THAT YOU CAN ADD!!!\n")
    for book in books:
        print("Book ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Details: {}".format(book[2]))
        print("Author: {}".format(book[3]))
        print()
    return

# This function adds a book to a users wishlist


def add_book_to_wishlist(cursor, user_id, book_id):
    try:
        insertWishlist = (
            "INSERT INTO wishlist(user_id,book_id) VALUES ({},{});".format(user_id, book_id))
        cursor.execute(insertWishlist)
    # Unique Constraint from database
    except mysql.connector.IntegrityError:
        print("ERROR: DUPLICATE ENTRY")
    # Bad input
    except mysql.connector.Error:
        print("DATABASE ERROR: INVALID ENTRY")
    return

# This function will show all the books in the users wishlist


def show_wishlist(cursor, user_id):
    selectUserWishlist = (
        "SELECT b.book_id, b.book_name, b.detailsV, author FROM book AS b INNER JOIN wishlist AS w ON b.book_id = w.book_id INNER JOIN user AS u ON w.user_id = u.user_id WHERE u.user_id = {};".format(user_id))
    cursor.execute(selectUserWishlist)
    books = cursor.fetchall()

    print("\nDISPLAY BOOKS FROM WISHLIST\n")
    for book in books:
        print("Book ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Details: {}".format(book[2]))
        print("Author: {}".format(book[3]))
        print()
    return

# This function is the wishlist menu


def wishlist_menu(user_id):
    userInput = ''
    while userInput != '3':
        print("\nWISHLIST MENU")
        userInput = input(
            "\nPlease enter one of the following:\n1 = Show Wishlist\n2 = Add Book\n3 = Main Menu\n")

        # Show wishlist will show the users wishlist
        if userInput == '1':
            db = connectSQL()
            cursor = db.cursor()
            show_wishlist(cursor, user_id)
            db.close()
        # Add book will add a book to a users wishlist
        elif userInput == '2':
            # Fist display the books to add
            db = connectSQL()
            cursor = db.cursor()
            show_books_to_add(cursor, user_id)

            # Then prompt the user for a bookId to add a book to wishlist
            bookId = input("Please give a book Id that you wish to add:\n")
            add_book_to_wishlist(cursor, user_id, bookId)
            db.commit()
            db.close()
        # Back Input
        elif userInput != '3':
            print("ERROR: INVALID ENTRY")
    # Exit back to Main Menu
    return

# This function will validate a user's ID by accessing the database with the given ID


def validate_user():
    accountNumber = input("\nPlease give your user ID number:\n")
    db = connectSQL()
    cursor = db.cursor()

    try:
        cursor.execute(
            "SELECT user_id FROM user WHERE user_id = {};".format(accountNumber))
        user = cursor.fetchone()
        db.close()
        # Return User ID
        if user != None:
            return user[0]
    # SQL exception with back input
    except mysql.connector.Error:
        print("DATABASE ERROR: INVALID ENTRY")
    # No user ID
    return

# This function is the Account Menu


def show_account_menu():
    # Validate User by getting user ID for input to the database and return user ID
    accountNumber = validate_user()

    # No user ID so proceed to Main Menu
    if accountNumber == None:
        print("ERROR: INVALID USER")
        return
    # Valid User ID to proceed to wishlist menu
    else:
        wishlist_menu(accountNumber)
    return


# This is the main function of the program which access the menu functionality
menu = ''
while menu != '4':
    # Main Menu
    menu = show_menu()

    # Returned My Account from menu's input to proceed to account menu
    if menu == '3':
        show_account_menu()
