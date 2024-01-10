#!/usr/bin/python3
"""
This is a function that appends a string in a file
"""


def append_write(filename="", text=""):
    """
    this function opens a file that alread exists and appends
    a string of text to it, this doesn't overrite the content
    of the file if it isn't empty
    """
    with open(filename, "a") as file:
        character = file.write(text)
    return character
