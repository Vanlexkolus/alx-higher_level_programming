#!/usr/bin/python3
"""
a class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns the
    rectangle perimeter:
    if width or height is equal to 0, perimeter is equal to 0

    """
    def __init__(self, width=0, height=0):
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
            self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("value must be an integer")
        elif value < 0:
            raise ValueError("value must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
