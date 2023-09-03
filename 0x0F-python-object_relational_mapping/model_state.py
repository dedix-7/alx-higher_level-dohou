#!/usr/bin/python3

"""
A Python file that contains the class definition of a State
and an instance Base = declarative_base():
State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated,
unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with
maximum 128 characters and can’t be null
You must use the module SQLAlchemy
Your script should connect to a MySQL server running on localhost
at port 3306
WARNING: all classes who inherit from Base must be imported before
calling Base.metadata.create_all(engine)
"""

# Import statements
from sys import argv
from sqlalchemy import create_engine, String, Integer, Column, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    """
    A State class that inherits from Base, and links to the MySQL table states
    Attributes:
        id: A column of an auto-generated, unique integer,
        can’t be null and is a primary key
        name: A column of a string with maximum 128 characters
        and can’t be null
    """
    __tablename__ = "states"    # Linking the State class to the states table.
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, id, name):
        """
        Initializing the class
        """
        self.id = id
        self.name = name


"""
# Storing input from standard input
username = argv[1]
password = argv[2]
database = argv[3]
port = 3306

# Connecting to the database
engine = create_engine("mysql+mysqldb://{}:{}@localhost:\
        {}/{}".format(username, password, port, database), echo=True)
Base.metadata.create_all(engine)    # Creates the State table
Session = sessionmaker(bind=engine)
session = Session()
"""
