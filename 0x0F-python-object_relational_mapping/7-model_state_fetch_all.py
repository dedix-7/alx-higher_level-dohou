#!/usr/bin/python3

"""
A Python script that lists all State objects from the database hbtn_0e_6_usa.
The script takes that lists all State objects from the database hbtn_0e_6_usa
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
The results must be displayed as they are in the example below
Your code should not be executed when imported
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


# Initializing the search...
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    port = 3306

    # Connecting to and initializing the engine
    db_url = "mysql+mysqldb://{}:{}\
            @localhost:{}/{}".format(username, password, port, database)
    engine = create_engine(db_url, pool_pre_ping=True)
    # 'pool_pre_ping=True' is used to test the connectivity of pooled database
    # connections before they're handed off to the application.

    # Creating a session to be used for our query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying and printing the States objects
    for result in session.query(State).order_by(State.id).all():
        print("{}: {}".format(result.id, result.name))

    # Closing the engine session
    # session.close()
