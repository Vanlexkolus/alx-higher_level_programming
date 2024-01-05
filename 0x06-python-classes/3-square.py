#!/usr/bin/python3
"""
class for the square
"""


class Square:
    """
    The objects for the class are deined below
    """

    def __init__(self, size=0):
        self.set_size(size)

    def get_size(self):
        return self.__size

    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
