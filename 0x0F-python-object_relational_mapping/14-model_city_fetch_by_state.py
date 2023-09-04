#!/usr/bin/python3

"""
A Python script that prints all City objects from the
database hbtn_0e_14_usa
Your script should take 3 arguments: mysql username,
mysql password and database name
You must use the module SQLAlchemy
You must import State and Base from model_state -
from model_state import Base, State
Your script should connect to a MySQL server running on
localhost at port 3306
Results must be sorted in ascending order by cities.id
Results must be display as they are in the example below
(<state name>: (<city id>) <city name>)
Your code should not be executed when imported
"""

from sys import argv
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Querying for all City objects
    results = session.query(State, City).join(City, State.id == City.state_id)\
        .order_by(asc(City.id)).all()
    # Sorting the results
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Closing the engine session
    session.close()
