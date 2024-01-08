#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order

    Args:
        my_list: A list
    """
    if my_list = []:
        return None
    reversed_list = my_list[::-1]
    length_reversed = len(reversed_list)
    for i in range(length_reversed):
        print("{:d}".format(reversed_list[i]))
