#!/usr/bin/python3

"""
A Python file that contains the class definition of a City
and an instance Base = declarative_base():
- State class:
- inherits from Base
- links to the MySQL table cities
- class attribute id that represents a column of an auto-generated,
- unique integer, can’t be null and is a primary key
- class attribute name that represents a column of a string with
- maximum 128 characters and can’t be null
- class attribute state_id that represents a column of an integer,
- can’t be null and is a foreign key to states.id
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost
at port 3306
WARNING: all classes who inherit from Base must be imported before
calling Base.metadata.create_all(engine)
"""

# Import statements
# from sys import argv
# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
from sqlalchemy import String, Integer, Column, ForeignKey
from model_state import Base


class City(Base):
    """
    A City class that inherits from Base (imported from model_state),
    and links to the MySQL table cities
    Attributes:
        id: A column of an auto-generated, unique integer,
        can’t be null and is a primary key.
        name: A column of a string with maximum 128 characters
        and can’t be null.
        states_id: A column of an integer, can’t be null and is a
        foreign key to states.id.
    """
    __tablename__ = 'cities'    # Linking the City class to the cities table.
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)


"""
# Storing input from standard input
username = argv[1]
password = argv[2]
database = argv[3]
port = 3306

# Connecting to the database
engine = create_engine("mysql+mysqldb://{}:{}@localhost:\
        {}/{}".format(username, password, port, database), echo=True)
Base.metadata.create_all(engine)    # Creates the Cities table
# Session = sessionmaker(bind=engine)
# session = Session()
"""
