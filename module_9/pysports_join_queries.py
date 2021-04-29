'''
Kaymon McCain
Assignment 9.2
4/29/2021

https://github.com/kaymonCodeM/csd-310.git
'''
import mysql.connector
from mysql.connector import errorcode


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
    print("\n")

    mycursor = mydb.cursor()
    print("-- DISPLAYING PLAYER RECORDS --")
    mycursor.execute(
        "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team on player.team_id=team.team_id;")
    players = mycursor.fetchall()
    for player in players:
        print("Player Id: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print()

    input("\n\nPress any key to continue...")

    mydb.close()
