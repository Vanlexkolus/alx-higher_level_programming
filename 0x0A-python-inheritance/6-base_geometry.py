#!/usr/bin/python3
"""
This is a class that whith a method  that raises
an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """
    This is a method that raises and Exception error
    """
    def area(self):
        """
        This method taken in no variable
        """
        raise Exception("area() is not implemented")
