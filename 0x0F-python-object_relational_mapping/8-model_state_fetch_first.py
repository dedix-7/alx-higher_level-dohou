#!/usr/bin/python3

"""
A Python script that prints the first State object
from the database hbtn_0e_6_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running
on localhost at port 3306
The state you display must be the first in states.id
You are not allowed to fetch all states from the database before
displaying the result
The results must be displayed as they are in the example below
If the table states is empty, print Nothing followed by a new line
Your code should not be executed when imported
Your code should not be executed when imported
"""

from sys import argv
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


# Initializing the search...
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    port = 3306

    # Connecting to and initializing the engine
    db_url = "mysql+mysqldb://{}:{}@localhost:\
            {}/{}".format(username, password, port, database)
    engine = create_engine(db_url, pool_pre_ping=True)

    # Creating a session to be used for our query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying and printing the first States object
    result = session.query(State).order_by(asc(State.id))[:1]
    """
    The line of code above is a Python list slicing syntax
    in the context of SQLAlchemy queries, it translates to SQL's LIMIT
    This statement will fetch only the first result
    Note: Unlike raw Python lists where slicing returns another list
    (even if it's a slice of a single element), in SQLAlchemy, this
    slicing technique on a query still gives you a list. Therefore, even
    if you're fetching a single item, the result will still be in
    a list format with that one item.
    We can also implement the code above in one line:
    # result = session.query(State).order_by(asc(State.id)).first()
    """
    if result:
        print("{}: {}".format(result[0].id, result[0].name))
    else:
        print("Nothing\n")

    # Closing the engine session
    # session.close()
