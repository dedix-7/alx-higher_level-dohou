#!/usr/bin/python3

"""
A Python script that  lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
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
    query = ("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    cursor.execute(query)

    # Returning results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    myDB.close()
