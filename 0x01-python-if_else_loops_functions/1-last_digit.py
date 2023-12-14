#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
myString = str(number)    # typecast number to string
lastDigit = int(myString[-1])   # get last digit of number
print("Last digit of {} is {} ".format(number, lastDigit), end="")
if lastDigit > 5:
    print("and is greater than 5")
elif lastDigit == 0:
    print("and is 0")
elif lastDigit < 6 and number != 0:
    print("and is less than 6 and not 0")
