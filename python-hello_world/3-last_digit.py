#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit= int(repr(number[-1]))
if number > 5:
   print('last digit of',number, 'is', last_digit, 'and is 0')