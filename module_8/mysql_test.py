import mysql.connector
from mysql.connector import errorcode


mydb = mysql.connector.connect()
try:
    config = {"host": "localhost", "user": "root", "password": "ShowMeTheShadow402!",
              "database": "pysports", "raise_on_warnings": True}
    mydb = mysql.connector.connect(**config)
    print("\n Database user {} connected MySQL on host {} with database {}.".format(
        config["user"], config["host"], config["database"]))
    input("\n\n  Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_KEYRING_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")
    else:
        print(err)
finally:
    mydb.close()
