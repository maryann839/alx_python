#!/usr/bin/env python3class Square:
"""
this is the class Square
"""
 
class Square:
    """
    specifying the attributes using __init__ 
    """ 
    def __init__(self, size):
        """
        initializing a square instance

        parameter - size
        no type / value verification was used
        """
        self.__size = size
    """
    getters
    """
    def get_size(self):
        return self.__size
    
    def set_size(self, value):
            self.__size = value

square1 = Square()
print("Size :", square1.get_size())




