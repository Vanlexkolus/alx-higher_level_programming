#!/usr/bin/python3
"""
This is a function that reads a file in this directory
"""


def read_file(filename=""):
    """
    This function reads a text file (UTF8) and prints it to stdout
    """
    filename = str(filename)
    with open(filename, "r") as file:
        size = 50
        read_file = file.read(size)
        while len(read_file) > 0:
            print(read_file, end="")
            read_file = file.read(size)
    print("")
