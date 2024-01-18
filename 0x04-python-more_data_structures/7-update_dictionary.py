#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds key/value in a dictionary.
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created

    Args:
        a_dictionary (dict): A dictionary
        key (str): a key that could modify the dictionary
        value (any): the value that could be replaced or created
    """
    a_dictionary[key] = value
    return a_dictionary
