#!/usr/bin/python3
""" A class that inherits 5-base_geometry.py from previous file"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ A basegeometry class"""

    def area(self):
        """ Not implemented """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
         """ Vlaideate the value 
         Args:
            name (str): the name of the value 
            value(int): the value to be validated
         
         Raises 
            TypeError if not an interger
            NameError if not a string"""
         
         if not isinstance(value, int):
             raise TypeError("{} must be an integer".format(name))
         if value <= 0:
             raise ValueError("{} must be greater than 0".format(name))
         
    def __init__(self, width, height):
        """ instantiation of wuidth and height"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height) 
