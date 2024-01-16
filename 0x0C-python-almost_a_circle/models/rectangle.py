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
    def width(self, new_wid):
        """
        This is the setter
        """
        if type(new_wid) != int:
            raise TypeError("width must be an integer")
        elif new_wid <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_wid

    @property
    def height(self):
        """
        This is the getter
        """
        return self.__height

    @height.setter
    def height(self, newH_val):
        """
        This is the setter
        """
        if type(newH_val) != int:
            raise TypeError("height must be an integer")
        elif newH_val <= 0:
            raise ValueError("height must be > 0")
        self.__height = newH_val

    @property
    def x(self):
        """
        This is the getter
        """
        return self.__x

    @x.setter
    def x(self, x_val):
        """
        This is the setter
        """
        if type(x_val) != int:
            """raise TypeError("Not an int")"""
        elif x_val < 0:
            raise ValueError("x must be >= 0")
        self.__x = x_val

    @property
    def y(self):
        """
        This is the getter
        """
        return self.__y

    @y.setter
    def y(self, y_val):
        """
        This is the setter
        """
        if type(y_val) != int:
            """raise TypeError("Not an int")"""
        elif y_val < 0:
            raise ValueError("y must be >= 0")
        self.__y = y_val
