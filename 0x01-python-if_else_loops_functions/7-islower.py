#!/usr/bin/python3
def islower(c):
    """
    A function that checks if its argument is in
    lowercase or uppercase
    """
    if len(c) == 1:
        ascii_value = ord(c)
        if 97 <= ascii_value <= 122:
            return True
        else:
            return False
    else:
        pass
