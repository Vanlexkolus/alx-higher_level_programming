#!/usr/bin/python3
"""
This is a function that prints a squar
"""


def print_square(size):
    """
    This function takes in only a single argument which
    is the size of the squre. The square is printed with
    the '#' character
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for x in range(size):
            for z in range(size):
                print("#", end=" ")
            print()
