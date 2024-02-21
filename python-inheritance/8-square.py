#!/usr/bin/python3
""" A class that inherits 7-rectangle.py from previous file"""
Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """ A square class using basegeometry class
        A square class using basegeometry class"""
    
    def __dir__(cls) -> None:
        """list all attribute except the __init_subclass__"""
        attributes = super().__dir__()
        dir_to_return = []
        for attribute in attributes:
            if attribute != "__init_subclass__":
                dir_to_return.append(attribute)
        return dir_to_return


    def __init__(self, size):
        """ instantiation of size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
     

    