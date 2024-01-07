#!/usr/bin/python3
"""
defined a class named Rectangle and this class
is a blueprint for printing any rectangle
"""


class Rectangle:
    """
    wrote a method using setter and getter to
    print a shape of a rectangle from an '#' symbol
    where the paremeters 'Height' and 'Width' are the
    things being collected and must be an integer
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
            self.__width = width
            self.__height = height

    def __str___(self):
        if self.__height > 0 and self.__width > 0:
            ang = ""
            for val in range(self.__height):
                if val < (self.__height - 1):
                    ang += "#" * self.__width + "\n"
                else:
                    ang += "#" * self.__width
            return ang
        else:
            return ""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("value must be an int")
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
            raise TypeError("value must be an int")
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
