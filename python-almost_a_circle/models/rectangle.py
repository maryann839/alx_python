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
         """
         validation of the model"""
         self.__validate_positive(value, 'width')
         """
         validation of the model"""
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
         """
         validation of the model"""
         self.__validate_positive(value, 'height')
         """
         validation of the model"""
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
         """
         validation of the model"""
         self.__validate_non_negative(value, 'x')
         """
         validation of the model"""
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
         """
         validation of the model"""
         self.__validate_non_negative(value, 'y')
         """
         validation of the model"""
         self.__y = value
    
    def area(self):
       """
    setter for private attributes width 
    this shows the accesibility of the private attribute width
    a setter is also assigned to it"""
       return  self.__width * self.__height
    
    """
    dislpay section"""
    def display(self):
     """
     replace the rectangle instanc with #
    """
     for _ in range(self.y):
          print()
     for _ in range(self.height):
          print(" "* self.x + "#"* self.width)

    """
    string """
    def __str__(self):
        """
        setter for private attributes width 
        this shows the accesibility of the private attribute width
        a setter is also assigned to it"""
         
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    
    """
    method of validation
    """
    def __validate_interger(self, value, attribute_name):
         """
         validation of the model"""
         if not isinstance(value, int):
              """
         validation of the model"""
              raise TypeError(f'{attribute_name} must be an integer')
    """
         validation of the model"""    
    def __validate_positive(self, value, attribute_name):
       """
         validation of the model"""
       if value <=0:
          """
         validation of the model"""
          raise ValueError(f'{attribute_name} must be > 0')
       
    """
         validation of the model"""
    def __validate_non_negative(self, value, attribute_name):
       """
         validation of the model"""
       if value < 0:
          """
         validation of the model"""
          raise ValueError(f'{attribute_name} must be >= 0')
    
    def update(self, *args, **kwargs):
        """ Update attributes"""
        if args:
            self.id = args[0] if len(args) > 0 else self.id
            self.width = args[1] if len(args) > 1 else self.width
            self.height = args[2] if len(args) > 2 else self.height
            self.x = args[3] if len(args) > 3 else self.x
            self.y = args[4] if len(args) > 4 else self.y
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
            
    



