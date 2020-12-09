#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
if number < 0:
    lastdigit= lastdigit * -1
string = "Last digit of {} is {}".format(number, lastdigit)
if lastdigit > 5:
    print(string + " and is greater than 5")
elif lastdigit == 0:
    print(string + " and is 0")
else:
    print(string + " and is less than 6 and not 0")

