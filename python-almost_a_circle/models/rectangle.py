"""
a class Rectangle that inherits from a base"""

from models.base import Base

class Rectangle(Base):
    """
    class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ call the constructor of the base"""
        super().__init__(id)

        """
        private attributes of the class"""
        self.__width =width
        self.__height = height
        self.__x = x 
        self.__y = y
    """
    a fuction to get the private attributes
    getters for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
    def get_width(self):
         """
        a fuction to get the private attributes
        getters for private attributes width 
        this shows the accesibility of the private attribute width
        a setter is also assigned to it"""
         return self.__width
    
    """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
    def set_width(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
        # self.__validate_interger(value, 'width')
        # self.__validate_positive(value, 'width')
         self.__width = value
    
    """
    getters and setters for all private attributes"""

    """
    getter for private attributes, height"""
    def get_height(self):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         return self.__height

    """
    setter for private attributes height """
    def set_height(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         self.__height = value

    """
    getters for private attributes, x"""
    def get_x(self):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         return self.__x

    """
    setters for private attributes x """
    def set_x(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         self.__x = value

    """
    getters for private attributes, y"""
    def get_y(self):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         return self.__x
   
    """
    Setters for private attributes, y"""
    def set_y(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         self.__x = value
    
    def area(self):
       """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
       return  self.__width * self.__height
    """
    string """
    def __str__(self):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         return f"Rectangle #{self.id}: width={self.__width}, height={self.__height}, x={self.__x}, y={self.__y}, area={self.area()}"

    
    """
    method of validation
    """
   
    
    



