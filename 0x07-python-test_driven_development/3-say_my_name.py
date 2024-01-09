#!/usr/bin/python3
"""
This is a function that prints the arguments
in a given string
"""


def say_my_name(first_name, last_name=""):
    """
    This function checks the input argument type and returns
    it, if it's not a string, it raises a TypeError.
    This function takes in two arguments (first_name and last_name)
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
