#!/usr/bin/python3
"""
created a class named Square
"""

class Square:
    """
    wrote the methods below that check's if the size is an int or if it's not greater than zero
    """
    def __init__(self, size=0):
        self.set_size(size)

    def get_size(self):
        return self.__size
    
    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError ("Please input an integer")
        elif size < 0:
            raise ValueError("The size should be greater tthan 0")
        else:
            self.__size = size
