#!/usr/bin/python3
"""
A Program that inports the function add
from a file add_0.py and prints the result
of the addition of 1 and 2
"""
if __name__ == "__main_":
    from add_0 import add
    
    # Define variables
    a = 1
    b = 2
    
    # Typecasting
    a = int(a)
    b = int(b)

    # Printing the result
    print("{} + {} = {}".format(a, b, add(a, b)))
