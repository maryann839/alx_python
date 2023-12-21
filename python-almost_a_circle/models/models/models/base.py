"""
creating bass class
"""

class Base:
    """
    private class attributes
    """
    __nb_objects = 0

    """
    class instructor
    """
    def __init__(self, id=None):
     """
     conditions
     """
     if id is not None:
        """
        interger or any data type
        """
        self.id = id
     else:
        """
        increment __nb_objects"""
        Base.__nb_objects += 1
        """
        equate id to __nb_objects"""
        self.id = Base.__nb_objects 




