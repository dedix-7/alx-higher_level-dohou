#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary.

    Args:
        a_dictionary (dict): a dictionary
        key (str, optional): a key of a_dictionary. Defaults to "".
    """
    if key in a_dictionary:
        del a_dictionary[key]
    else:
        pass
    return a_dictionary
