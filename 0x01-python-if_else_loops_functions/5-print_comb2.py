#!/usr/bin/python3
for i in range(100):
    if i <= 9:
        print("{:02d}, ".format(i), end="")
    elif i == 99:
        print(i)
    else:
        print("{}, ".format(i), end="")
