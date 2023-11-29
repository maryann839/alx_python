#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
Last_digit= abs(number)% 10
if Last_digit > 5:
   print('Last digit of', number, 'is', Last_digit , 'and is greater than 5')
elif Last_digit == 0:
   print('Last digit of', number, 'is', Last_digit , 'and is 0')
else:
    pass
import sys 