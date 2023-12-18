#!/usr/bin/python3
for i in range(97, 122):
    # while i != 101 or i != 113:
    # print("{:c}".format(97 + i), end="")
    if i == 101 or i == 113:
        continue
    else:
        print("{:c}".format(i), end="")
