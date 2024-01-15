#!/usr/bin/python3
"""
Module 10-square
This is class square that inherit from class Rectangle

The class Rectanle will be imported
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherit from Rectabgle who inherit from base class
    methods:
        __init__(self, size)
    """

    def __init__(self, size):
        """Initilaize size
        Args:
            size (int): private attribute
        """

        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def __str__(self):
            """prints [Rectangle] <width>/<height>"""
            return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                             self.__size, self.__size)
