#!/usr/bin/python3
"""
This is a class that has a function that returns
that returns the list of available attributes and
methods of an object
"""


def lookup(obj):
    """
    This method returns the list of available
    attributes and methods of an object using the dir()
    built-in function
    """
    return (dir(obj))
