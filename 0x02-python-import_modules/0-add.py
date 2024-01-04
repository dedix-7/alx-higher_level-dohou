#!/usr/bin/python3

if __name__ == "__main__":

    from add_0 import add

    # Define variables
    a = 1
    b = 2

    # Typecasting
    a = int(a)
    b = int(b)

    # Printing the result
    print("{} + {} = {}".format(a, b, add(a, b)))
