#!/usr/bin/python3
def islower(c):
    """
    A function that checks if its argument is in
    lowercase or uppercase
    """
    ascii_value = ord(c)
    if ascii_value >= 97 and ascii_value <= 122:
        return True
    else:
        return False
