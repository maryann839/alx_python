#!/usr/bin/python3
""" A class that inherits 5-base_geometry.py from previous file"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ A rectangle class using basegeometry class"""

    def __dir__(cls) -> None:
        """list all attribute except the __init_subclass__"""
        attributes = super().__dir__()
        dir_to_return = []
        for attribute in attributes:
            if attribute != "__init_subclass__":
                dir_to_return.append(attribute)
        return dir_to_return



    def __init__(self, width, height):
        """ instantiation of width and height"""
        super().integer_validator("width", width)
        self.__width =  width
        super().integer_validator("height", height) 
        self.__height = height


    def area(self):
        """ print the area of the rectangle"""
        return self.__width * self.__height
    
    def __str__(self):
        """Return the string description of the rectrangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    
    def print(self):
        """ print the rectngle """
        print(str(self))