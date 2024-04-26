#!/usr/bin/python3

"""
A Python script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa.
Your script should take 3 arguments: mysql username, mysql
password and database name.
You must use the module SQLAlchemy.
You must import State and Base from model_state -
from model_state import Base, State.
Your script should connect to a MySQL server running on
localhost at port 3306.
Print the new states.id after creation.
Your code should not be executed when imported.
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

    # Creating and adding a new State object - "Louisiana"
    new_object = State(name="Louisiana")
    session.add(new_object)
    session.commit()

    # Printing the id of the new State object ("Louisiana")
    print("{}".format(new_object.id))

    # Closing the engine session
    session.close()
