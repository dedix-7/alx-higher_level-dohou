#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary (dict): a dictionary
    """
    new_dict = {x: (a_dictionary[x] * 2) for x in a_dictionary}
    return new_dict
