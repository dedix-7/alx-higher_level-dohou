#!/usr/bin/python3
def uppercase(str):
    """
    A function that returns the uppercase
    version of strings
    """
    # ascii_value = ord(str)
    # length = len(str)
    # ascii_value >= 97 and ascii_value <= 122:
    myStr = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            myStr += chr(ord(str[i]) - 32)
            continue
        myStr += str[i]
    print("{}".format(myStr))
