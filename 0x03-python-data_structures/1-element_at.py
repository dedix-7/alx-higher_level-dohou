#!/usr/bin/python3
def element_at(my_list, idx):
    """
    A function that returns an
    element from a list like in C

    Args:
        my_list: A list looped through
        idx: the index to be returned
    """
    length = len(my_list) - 1
    if idx not in range(length):
        return None
    elif idx != abs(idx):
        return None
    else:
        return my_list[idx]
