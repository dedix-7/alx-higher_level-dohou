#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values multiplied
    by a number without using any loops.

    Args:
        my_list (list, optional): A list. Defaults to [].
        number (int, optional): Multiplies the list. Defaults to 0.
    """
    # myNumber = number
    return list(map(lambda x, myNumber=number: x * myNumber, my_list))
