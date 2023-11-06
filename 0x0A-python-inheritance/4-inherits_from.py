#!/usr/bin/python3
""" Module: 4-inherits_from
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class inherited
    (directly or indirectly)
    obj: an object
    a_class: a class
    Returns None
    """
    """
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    else:
        return False
    """
    # return (type(obj) is not a_class and issubclass(type(obj), a_class))
    return (type(obj) is not a_class and isinstance(obj, a_class))
