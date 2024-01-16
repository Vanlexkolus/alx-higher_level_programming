#!/usr/bin/python3
"""
This is a module containing a class: Rectangle that
inherits the class: Base
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a class that inherits the methods
    of the class base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This init method takes in 5 arguments
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        This is the getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        This is the setter
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        This is the getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This is the setter
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        This is the getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        This is the setter
        """
        if type(value) != int:
            """raise TypeError("Not an int")"""
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        This is the getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        This is the setter
        """
        if type(value) != int:
            """raise TypeError("Not an int")"""
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        This is a public method that returns the
        area of the rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        This is a method that prints a rectangle
        """
        for y in range(self.__y):
            print("")
        for horizontal in range(self.__height):
            for i in range(self.__x):
                print(" ", end="")
            for vertical in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        The __str__ method returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x,
                                                self.__y, self.__width,
                                                self.__height)
