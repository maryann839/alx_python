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
        self.__width = 0
        self.width = width
        self.__height = 0
        self.height= height
        self.__x = 0
        self.x = x
        self.__y = 0
        self.y = y
    """
    a fuction to get the private attributes
    getters for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
    @property
    def width(self):
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
    @width.setter
    def width(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         self.__validate_interger(value, 'width')
         self.__validate_positive(value, 'width')
         self.__width = value
    
    """
    getters and setters for all private attributes"""

    """
    getter for private attributes, height"""
    @property
    def height(self):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         return self.__height

    """
    setter for private attributes height """
    @height.setter
    def height(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         self.__validate_interger(value, 'height')
         self.__validate_positive(value, 'height')
         self.__height = value

    """
    getters for private attributes, x"""
    @property
    def x(self):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         return self.__x

    """
    setters for private attributes x """
    @x.setter
    def x(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         self.__validate_interger(value, 'x')
         self.__validate_non_negative(value, 'x')
         self.__x = value

    """
    getters for private attributes, y"""
    @property
    def y(self):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         return self.__y
   
    """
    Setters for private attributes, y"""
    @y.setter
    def y(self, value):
         """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
         self.__validate_interger(value, 'y')
         self.__validate_non_negative(value, 'y')
         self.__y = value
    
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
    def __validate_interger(self, value, attribute_name):
         if not isinstance(value, int):
              raise TypeError(f'{attribute_name} must be an integer')
         
    def __validate_positive(self, value, attribute_name):
       if value <=0:
          raise ValueError(f'{attribute_name} must be > 0')
       
    def __validate_non_negative(self, value, attribute_name):
       if value <=0:
          raise ValueError(f'{attribute_name} must be >= 0')
   
    
    



