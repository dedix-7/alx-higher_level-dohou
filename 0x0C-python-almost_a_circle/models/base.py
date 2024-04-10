#!/usr/bin/python3
"""
The Base class
"""


class Base:
    """
    The Base Class:
        The Base of all other classes
        This class manages id attribute of future classes

    Attributes:
        __nb_objects: Stores the ids
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        The instance method for the Base class
        """
        if type(id) != None:
            id = None
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
