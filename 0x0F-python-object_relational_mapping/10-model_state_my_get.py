#!/usr/bin/python3

"""
A Python script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa.
Your script should take 4 arguments: mysql username, mysql
password, database name and state name to search (SQL injection free).
You must use the module SQLAlchemy.
You must import State and Base from model_state -
from model_state import Base, State.
Your script should connect to a MySQL server running on
localhost at port 3306.
You can assume you have one record with the state name to search.
Results must display the states.id
If no state has the name you searched for, display 'Not found'
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
    argum = argv[4]
    port = 3306

    # Connecting to and initializing the engine
    db_url = "mysql+mysqldb://{}:{}@localhost:\
            {}/{}".format(username, password, port, database)
    engine = create_engine(db_url, pool_pre_ping=True)

    # Creating a session to be used for our query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying and printing the first States object
    result = session.query(State).filter(State.name == argum).first()
    # result = session.query(State).filter(State.name.like('%a%')).all
    if result:
        print("{}".format(result.id))
    else:
        print("Not found")

    # Closing the engine session
    # session.close()
