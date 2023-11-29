#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
# this is a positive number
number = 98
if number > 0:
  print("{} is positive".format(number))
elif number == 0:
   print("{} is zero".format(number))
elif number < 0:
  print("{} is negative".format(number))
number = 98
if number != 0:
  print("TypeError")
import sys