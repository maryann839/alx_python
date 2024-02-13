#!/usr/bin/python3
"""
a class Square that inherits from a Rectangle"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ this class represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
     """ initialize a new square"""
     super().__init__(size, size, x, y, id)

    @property
    def size(self):
       """ get the size of the square"""
       return self.width
    
    @size.setter
    def size(self, value):
       """ setter for the size"""
       self.width = value
       self.height = value

    def __str__(self):
       """ Return the string """
       return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}" 


