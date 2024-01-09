#!/usr/bin/python3
"""
writing a meethod that adds two int or floats together
"""
def add_integer(a, b=98):
    """
    the following code is gonna check and raise errors
    if the following parameters are being breeched

    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
    return a + b
