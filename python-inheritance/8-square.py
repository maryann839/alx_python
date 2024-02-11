#!/usr/bin/python3
""" A class that inherits 7-rectangle.py from previous file"""
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """ A square class using basegeometry class
        A square class using basegeometry class"""

    def __init__(self, size):
        """ instantiation of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
     

    