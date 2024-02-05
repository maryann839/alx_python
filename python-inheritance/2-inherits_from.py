#!/usr/bin/python3
""" a function that returns True if the object is an 
instance of a class that inherited (directly or indirectly) from the specified class ;
 otherwise False. """

def inherits_from(obj, a_class):
    """check if the object is an instance of the specified class"""
    if type(obj) is a_class:
        return False
    else:
        for base_class in type.__bases__:
            if inherits_from(base_class, a_class):
                return True
        return False    