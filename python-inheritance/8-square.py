#!/usr/bin/python3
""" A class that inherits 7-rectangle.py from previous file"""
BaseGeometry = __import__('7-rectangle').BaseGeometry

class Square(BaseGeometry):
    """ A square class using basegeometry class
        A square class using basegeometry class"""

    def __init__(self, size):
        """ instantiation of size"""
        self.__size = self.integer_validator("size", size)
     

    def area(self):
        """ print the area of the rectangle"""
        return self.__width * self.__height    