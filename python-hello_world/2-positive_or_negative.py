#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
print(number, end=" ")
if number > 0:
  print("{} is positive".format(number))
elif number == 0:
   print("{} is zero".format(number))
elif number != 0:
  print("TypeError")
else:
  print("{} is negative".format(number))
# if number != 0:
#   print("TypeError")


