#!/usr/bin/python3
def print_last_digit(number):
    """
    A function that prints
    the last digits of a
    number
    """
    myString = str(number)
    last_letter = myString[-1]
    last_number = int(last_letter)
    print("{}".format(last_number), end="")
    return last_number
