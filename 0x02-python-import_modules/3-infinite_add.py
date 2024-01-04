#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv as arg
    length = len(arg) - 1
    total = 0
    for j in range(length):
        total += int(arg[j + 1])
    print("{}".format(total))
