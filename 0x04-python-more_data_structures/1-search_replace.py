#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element
    in a list by another in a new list

    Args:
        my_list (list): list to be moified
        search (int): integer to be replaced
        replace (int): integer replacing search
    """
    return list(map(lambda i: replace if i == search else i, my_list))
