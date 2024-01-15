#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is a class named Rectangle and it
    inherits from BaseGeomety
    """
    def __init__(self, width, height):
        """
        This init method takes in two args and it helps me with
        the project: Write a class Rectangle that inherits from BaseGeometry
        (7-base_geometry.py). (task based on 8-rectangle.py)
        Instantiation with width and height:
        def __init__(self, width, height):
        width and height must be private. No getter or setter
        width and height must be positive integers validated by
        integer_validator the area() method must be implemented
        print() should print, and str() should return, the
        following rectangle description: [Rectangle] <width>/<height>
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        extend parent area method
        """
        return self.__width * self.__height

    def __str__(self):
        """
        print [Rectangle] <width>/<height>
        """
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                self.__width, self.__height)
