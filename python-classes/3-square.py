#!/usr/bin/env python3class Square:

""" this involves the creation of a class that defines 
a square by a private  instance attributes, instantiation with  type/value
a type error included and no module was imported 
this involves the creation of a class that defines 
a square by a private  instance attributes, instantiation with  type/value
a type error included and no msodule was imported """

class Square:
     
     """ specifying the attributes using __init__ """

     def __init__(self, size=0):
        if not isinstance(size, int):
           raise TypeError("size must be an integer")
        elif size < 0:
           raise ValueError("size must be >= 0")
        else:
          self.__size = size
        

     @property
     def size(self):
        """ this assigns self.__size to size """
        return self.__size 
     
     @size.setter
     def size(self, value):
      if not isinstance(value, int):
           raise TypeError("size must be an integer")
      elif value< 0:
           raise ValueError("size must be >= 0")
      else:
         self.__size = value

     def area(self):
         """ this calculates the area of a square """
         return self.__size ** 2
     
     def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)


""" this calculates the area of a square  """
square1 = Square()

