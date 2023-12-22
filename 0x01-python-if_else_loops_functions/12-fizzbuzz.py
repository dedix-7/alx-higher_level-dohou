#!/usr/bin/python3
def fizzbuzz():
    """
    A function that prints the numbers
    1 to 100
    If number is a multiple of 3, print Fizz
    If number is a multiple of 5, print Buzz
    If number is a multiple of 15, print Fizzbuzz
    Else, print number
    """
    for i in range(1, 101):
        # Check if i is a multiple of 3
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
