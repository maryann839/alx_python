#!/usr/bin/python3
""" A class that inherits 7-rectangle.py from previous file"""
BaseGeometry = __import__('7-rectangle').BaseGeometry

class Rectangle(BaseGeometry):
  """ A square class using basegeometry class
  A square class using basegeometry class"""

  def __init__(self, width, height):
        """ instantiation of wuidth and height"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height) 

  def area(self):
        """ print the area of the rectangle"""
        return self.__width * self.__height    