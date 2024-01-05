#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv as arg
    from calculator_1 import add, sub, mul, div

    length = len(arg)
    operators = ["+", "-", "*", "/"]
    # a = int(arg[1])
    # oper = arg[2]
    # b = int(arg[3])

    if length != 4:
        print("Usage: {} <a> <operator> <b>".format(arg[0]))
        exit(1)
    else:
        a = int(arg[1])
        oper = arg[2]
        b = int(arg[3])
        if oper in operators:
            if oper == "+":
                print("{} {} {} = {}".format(a, oper, b, add(a, b)))
            elif oper == "-":
                print("{} {} {} = {}".format(a, oper, b, sub(a, b)))
            elif oper == "*":
                print("{} {} {} = {}".format(a, oper, b, mul(a, b)))
            else:
                print("{} {} {} = {}".format(a, oper, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
