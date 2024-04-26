#!/usr/bin/python3

"""
A Python script that deletes all State objects with
a name containing the letter a from the database hbtn_0e_6_usa.
Your script should take 3 arguments: mysql username, mysql
password and database name.
You must use the module SQLAlchemy.
You must import State and Base from model_state -
from model_state import Base, State.
Your script should connect to a MySQL server running on localhost at port 3306.
Your code should not be executed when imported.
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
    db_url = "mysql+mysqldb://{}:{}@localhost:\
            {}/{}".format(username, password, port, database)
    engine = create_engine(db_url, pool_pre_ping=True)

    # Creating a session to be used for our query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Searching for State objects containing 'a'
    delete_objects = session.query(State).filter(State.name.contains('a'))
    # Deleting the State objects that contain 'a'
    if delete_objects:
        for delete in delete_objects:
            session.delete(delete)
    session.commit()

    # Closing the engine session
    session.close()
