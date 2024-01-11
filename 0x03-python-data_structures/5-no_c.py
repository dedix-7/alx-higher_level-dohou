#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters 'c'
    and 'C' from a string
    """
    # Convert my_string to a list of characters
    # characters = list(my_string)
    # Create a new string
    new_string = ""
    length = len(my_string)
    for i in range(length):
        if my_string[i] != 'c' and my_string[i] != 'C':
            new_string += my_string[i]
    return new_string
