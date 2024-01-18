#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer)

    Args:
        my_list (list): Defaults to [].
    """
    # A list containing unique elements of the list
    # unique = list(set(my_list))
    # return reduce(lambda x, y: x + y, unique)
    # A list containing unique elements of the list
    unique = list(set(my_list))
    sum = 0
    for i in range(len(unique)):
        sum += unique[i]
    return sum
