#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
# print(number, end=" ")
if number > 0:
  print(" is positive")
elif number == 0:
   print(" is zero")
else:
  print(" is negative")
# if number != 0:
#   print("TypeError")


#Check if the number is positive, negative, or zero
print(f"{number} is {'positive' if number > 0 else 'zero' if number == 0 else 'negative'}")
