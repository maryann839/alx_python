#!/usr/bin/env python3class Square:

""" this involves the creation of a class that defines 
a square by a private  instance attributes, instantiation with  type/value
a type error included and no module was imported """

class Square:
     """ specifying the attributes using __init__ """
     def __init__(self, size=0):
        if not isinstance(size, int):
           raise TypeError("size must be an integer")
        elif size < 0:
           raise ValueError("size must be >= 0")
        """ this involves the creation of a class that defines 
        a square by a private  instance attributes, instantiation with  type/value
        a type error included and no module was imported """
        self.__size = 0
        self.size = size 

     def area(self):
        """ this calculates the area of a square  """
        """ this involves the creation of a class that defines 
        a square by a private  instance attributes, instantiation with  type/value
        a type error included and no module was imported """
        return self.__size ** 2

     @property
     def size(self):
        """ this assigns self.__size to size """
        """ this involves the creation of a class that defines 
        a square by a private  instance attributes, instantiation with  type/value
        a type error included and no module was imported """
        return self.__size 
""" this calculates the area of a square  """
square1 = Square()
