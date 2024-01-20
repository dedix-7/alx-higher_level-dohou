#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
    A function that deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): A dictionary
        value (str): value used to delete a key
    """
    list_dict_keys = list(a_dictionary.keys())
    for value_dict in list_dict_keys:
        if value == a_dictionary.get(value_dict):
            del a_dictionary[value_dict]
    return a_dictionary
