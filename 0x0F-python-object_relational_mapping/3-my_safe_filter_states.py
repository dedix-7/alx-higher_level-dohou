#!/usr/bin/python3

"""
A Python script that handles SQL Injections.
The script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
Your script should take 4 arguments: mysql username, mysql password,
database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv
# Using parametized queries, to ensure that user input is
# treated as data and not executable SQL.
# from sqlalchemy.sql import text

if __name__ == '__main__':
    """
    Connecting to the database and listing all the states in hbtn_0e_0_usa
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    myDB = MySQLdb.connect(
        host="localhost",
        user=username,
        port=3306,
        passwd=password,
        db=database
    )

    # Executing statement
    cursor = myDB.cursor()
    query = ("SELECT * FROM states WHERE name=%s ORDER BY states.id ASC")
    cursor.execute(query, (state_name,))
    # Add 'BINARY' keyword for case sensitivity.

    # Returning results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    myDB.close()
