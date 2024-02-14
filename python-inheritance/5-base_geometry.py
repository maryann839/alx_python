#!/usr/bin/python3
""" improving the geometry class from previous file"""

class BaseGeometry:
    """ A basegeometry class"""
    def __dir__(cls) -> None:
        """list all attribute except the __init_subclass__"""
        attributes = super().__dir__()
        dir_to_return = []
        for attribute in attributes:
            if attribute != "__init_subclass__":
                dir_to_return.append(attribute)
        return dir_to_return

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