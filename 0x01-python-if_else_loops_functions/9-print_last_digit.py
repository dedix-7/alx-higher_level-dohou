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
    """
    This code works very efficiently, but
    using modulo (%) to return the last digits
    of numbers is much more efficient:
    if number >= 0:
        myNumber = number % 10
    else:
        myNumber = abs(number % 10)
    print("{}".format(last_number), end="")
    return last_number
    """
