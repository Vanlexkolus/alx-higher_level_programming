#!/usr/bin/python3
"""
This is a class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This class inherits properties from the class Rectangle
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
