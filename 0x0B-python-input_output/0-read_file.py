#!/usr/bin/python3
"""
This is a function that reads a file in this directory
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout
    """
    filename = str(filename)
    with open(filename, "r", encoding="UTF-8") as file:
        read_file = file.read()
        print(read_file, end="")
