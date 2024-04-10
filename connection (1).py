# Define global variables for cursor and connection
import mysql
from mysql.connector import connect, Error
#from sqlite3 import connect

from fullcode import create_table, insert_data_from_csv

cursor = None
connection = None

def connect_to_mysql(host, user, password, database):
    try:
        connection = connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection  # Return the connection object
        else:
            print("Failed to connect to MySQL database")
            return None
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

#Functions to manipulate data
# .......
# .......

def main():
    host = "127.0.0.1"
    user = "root"
    password = "Nayan@12345"
    database = "new"

    # Connect to MySQL database
    connection = connect_to_mysql(host, user, password, database)
    if connection:
        create_table(connection)
       # insert_data_from_csv(connection, '/home/nineleaps/Downloads/all.csv')