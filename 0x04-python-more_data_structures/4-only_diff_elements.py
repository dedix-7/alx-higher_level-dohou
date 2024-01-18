#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set

    Args:
        set_1 (set): first set
        set_2 (set): second set
    """
    return (set_1 ^ set_2)
