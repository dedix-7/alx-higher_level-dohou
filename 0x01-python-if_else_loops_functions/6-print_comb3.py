#!/usr/bin/python3
for b in range(10):
    for c in range(10):
        if b == 8 and c == 9:
            print("{}{}".format(b, c))
        elif b != c and b < c:
            print("{}{}, ".format(b, c), end="")
        else:
            continue
