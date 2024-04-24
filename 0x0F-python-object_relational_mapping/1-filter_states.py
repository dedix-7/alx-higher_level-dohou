#!/usr/bin/python3

"""
A Python script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
The script should take 3 arguments: mysql username, mysql password and database
name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connecting to the database and listing all the states in hbtn_0e_0_usa
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    myDB = MySQLdb.connect(
        host="localhost",
        user=username,
        port=3306,
        passwd=password,
        db=database
    )

    # Executing statement
    cursor = myDB.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                   ORDER BY states.id ASC"""
                   )
    # Add 'BINARY' keyword for case sensitivity.

    # Returning results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Closing the cursor and the database connection
    cursor.close()
    myDB.close()
