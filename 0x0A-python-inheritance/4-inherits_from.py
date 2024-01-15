#!/usr/bin/python3
"""
This is a function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    This function takes in two args
    the obj and the class type
    """
    obj_class = type(obj)
    return issubclass(obj_class, a_class) and obj_class is not a_class
