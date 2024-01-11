#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a
    specific position without modifying
    the original list (like in C).

    Args:
        my_list: The list to be altered
        idx: Index of element to be altered
        element: Element to be altered
    """
    new_list = my_list[:]
    length = len(new_list) - 1
    if idx < 0:
        return new_list
    elif idx > length:
        return new_list
    else:
        new_list[idx] = element
    return new_list
