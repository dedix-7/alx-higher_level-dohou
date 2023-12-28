#!/usr/bin/python3
"""
A Python function that ceates
a copy of a string, and removes
a chatacter at the position n
using indexes
"""


def remove_char_at(str, n):
    # Convert the string to a list of characters
    # since strings in Python are immutable
    myCharList = list(str)
    # Check if n is of valid syntax
    if n >= 0 and n < len(str):
        # Delete the character of specific index
        del myCharList[n]
    # Joining the list back to a string
    finalStr = "".join(myCharList)
    return finalStr
