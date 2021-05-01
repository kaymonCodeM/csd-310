'''
Kaymon McCain
Assignment 9.3
4/29/2021

https://github.com/kaymonCodeM/csd-310.git
'''
import mysql.connector
from mysql.connector import errorcode

# This function will make a connection to mySQL database and return the connection


def connectSQL():
    mydb = mysql.connector.connect()
    try:
        config = {"host": "localhost", "user": "root", "password": "ShowMeTheShadow402!",
                  "database": "pysports", "raise_on_warnings": True}
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


# This function prints out the mySQL table player form the database
def printSQLPlayer():
    mydb = connectSQL()
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team on player.team_id=team.team_id;")
    players = mycursor.fetchall()
    for player in players:
        print("Player Id: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()
    mydb.close()


print("\n")

# Delete Smeagol if in the database and insert Smeagol
mydb = connectSQL()
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM player where player_id=21;")
mycursor.execute(
    "INSERT INTO player(player_id,first_name,last_name,team_id) VALUES(21,'Smeagol', 'Shire Folk', 1);")
mydb.commit()
mydb.close()

# Print out the results of the insert of Smeagol
print("-- DISPLAYING PLAYER AFTER INSERT --")
printSQLPlayer()

# Update Smeagol team_nmae to Team Sauron
mydb = connectSQL()
mycursor = mydb.cursor()
mycursor.execute("UPDATE player SET team_id = 2 WHERE player_id = 21;")
mydb.commit()
mydb.close()

# Print out the results from updating Smeagol's team
print("-- DISPLAYING PLAYER AFTER UPDATE --")
printSQLPlayer()

# Delete Smeagol
mydb = connectSQL()
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM player WHERE player_id=21;")
mydb.commit()
mydb.close()

# Print out the results after deleting Smeagol
print("-- DISPLAYING PLAYER AFTER DELETE --")
printSQLPlayer()

input("\n\nPress any key to continue...")
