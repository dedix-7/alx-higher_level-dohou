#!/usr/bin/python3
"""
A program that prints the ASCII alphabet,
in reverse order, alternating lowercase,
and uppercase, not followed by a new line.
"""

for i in reversed(range(97, 123)):
    # Checking if the alphabet is a lowercase
    # z is lowercase, and is of ASCII number 122
    if (i % 2 == 0):
        # This alphabet is to be lowercase
        # a += str(ord(i))
        print("{:c}".format(i), end="")
    else:
        # This letter is to be uppercase
        # a += str(ord(i))
        print("{:c}".format(i - 32), end="")
