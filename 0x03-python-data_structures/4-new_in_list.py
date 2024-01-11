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
    length = len(my_list) - 1
    if idx < 0:
        return copy(my_list)
    elif idx > length:
        return copy(my_list)
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list
