#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    A function that replaces an element of a
    list at a specific position like in C

    Args:
        my_list: The list to be used
        idx: Index to be replaced
        element: The element to be at my_list[idx]
    
    Return:
        my_list with my_list[idx] = element
    """
    length = len(my_list) - 1
    if idx < 0:
        return my_list
    elif idx > length:
        return my_list
    else:
        my_list[idx] = element
    return my_list
