#!/usr/bin/python3
def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.

    Args:
        a_dictionary (int): a description
    """
    if not a_dictionary:
        return None
    else:
        # max_key = None
        values_list = list(a_dictionary.values())
        max_value = values_list[0]
        # Using a loop to get the highest value, thus the key
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key
