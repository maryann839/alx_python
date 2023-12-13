#!/usr/bin/env python3class Square:
# creating  a class  
class Square:
    # specifying the attributes using __init__ 
   def __init__(self, size=0):
        self.__size = size
   def get_size(self):
       return self.__size
   def set_size(self, size):
        self.__size = size

square1 = Square(0)
print("Size :", square1.get_size())




