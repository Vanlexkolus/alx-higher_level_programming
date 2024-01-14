#!/usr/bin/python3
"""
This is a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    """
    This function takes in two args, an object and
    a class
    """

    return isinstance(obj, a_class)
