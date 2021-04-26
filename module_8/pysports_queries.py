import mysql.connector
from mysql.connector import errorcode


mydb = mysql.connector.connect()
try:
    config = {"host": "localhost", "user": "root", "password": "ShowMeTheShadow402!",
              "database": "pysports", "raise_on_warnings": True}
    mydb = mysql.connector.connect(**config)
    print("\n Database user {} connected MySQL on host {} with database {}.".format(
        config["user"], config["host"], config["database"]))
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
    mycursor.execute("SELECT team_id, team_name, mascot FROM team;")
    teams = mycursor.fetchall()

    print("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("Team ID: {}".format(team[0]))
        print("Team Name: {}".format(team[1]))
        print("Mascot: {}".format(team[2]))
        print()

    print("-- DISPLAYING PLAYER RECORDS --")
    mycursor.execute(
        "SELECT player_id, first_name, last_name, team_id FROM player;")
    players = mycursor.fetchall()
    for player in players:
        print("Player Id: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team ID: {}".format(player[3]))
        print()

    mydb.close()
