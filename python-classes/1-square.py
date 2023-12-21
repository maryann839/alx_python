class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
           raise TypeError("size must be an integer")
        elif size < 0:
           raise ValueError("size must be >- 0")
        self.__size = size

square1 = Square()



class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
           raise TypeError("size must be an integer")
        elif size < 0:
           raise ValueError("size must be >- 0")
        self.__size = size

square1 = Square()


# models/rectangle.py

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        # Call the constructor of the base class to manage the id attribute
        super().__init__(id)
        
        # Private instance attributes
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # Getter and setter for width
    @property
    def width(self):
        return self.__width

  
    Getter and setter for height
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return f"Rectangle #{self.id}: width={self.__width}, height={self.__height}, x={self.__x}, y={self.__y}, area={self.area()}"

# Example usage
if __name__ == "__main__":
    rectangle1 = Rectangle(5, 10)
    print(rectangle1)  # Output: Rectangle #1: width=5, height=10, x=0, y=0, area=50

    rectangle2 = Rectangle(3, 7, x=2, y=3, id=2)
    print(rectangle2)  # Output: Rectangle #2: width=3, height=7, x=2, y=3, area=21
