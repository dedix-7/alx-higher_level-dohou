#!/usr/bin/python3

"""
A Python script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
Your script should take 4 arguments: mysql username, mysql password,
database name and state name (SQL injection free!).
You must use the module MySQLdb (import MySQLdb).
Your script should connect to a MySQL server running on localhost at port 3306.
Results must be sorted in ascending order by cities.id
You can use only execute() once.
The results must be displayed as they are in the example below.
Your code should not be executed when imported.
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
    query = ("SELECT cities.name FROM cities JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC")
    cursor.execute(query, (state_name,))

    # Returning results
    results = cursor.fetchall()
    print(", ".join([row[0] for row in results]))

    # Close the cursor and connection
    cursor.close()
    myDB.close()
