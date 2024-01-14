#!/usr/bin/python3
"""
This is a function that returns 'True' if the object
is an instance of, or if the object is an instance
of a class that inherited from, the specified
class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    This method takes two args, the object
    and the class type
    """
    inheritesType = isinstance(obj, a_class)
    return inheritesType
