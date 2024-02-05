#!/usr/bin/python3
""" This is a function that returns True if the object is an 
instance of, or if the object is an instance of a class that inherited from, 
the specified class ; otherwise False. """

def is_kind_of_class(obj, a_class):
    """check if the object is an instance of the specified class
      or inherited from a class"""
    return isinstance(obj), a_class