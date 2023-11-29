#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sub = -1
if number < 0:
    dig = number * sub
else:
    sub = 1
    dig = number
last_dig = (dig % 10) * sub
if last_dig > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_dig))
elif last_dig == 0:
    print("Last digit of {} is {} and is 0".format(number, last_dig))
elif 0 < last_dig < 6:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_dig))
