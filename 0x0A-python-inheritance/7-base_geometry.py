#!/usr/bin/python3
"""
This is a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    This class has two methods, first raise an Exception
    with the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This method takes two variables and it validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0
        """
        self.name = name
        self.value = value
        if type(value) != int:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")
