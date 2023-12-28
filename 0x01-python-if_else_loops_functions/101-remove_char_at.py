#!/usr/bin/python3
"""
A Python function that ceates
a copy of a string, and removes
a chatacter at the position n
using indexes
"""


def remove_char_at(str, n):
    myCharList = list(str)
    if n >= 0 and n < len(str):
        del myCharList[n]
    finalStr = "".join(myCharList)
    return finalStr
