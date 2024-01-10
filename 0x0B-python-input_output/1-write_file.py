#!/usr/bin/python3
"""
This is a functin that writes into a new file
"""


def write_file(filename="", text=""):
    """
    This method takes in a string of text and writes it in a
    a folder, if the foldr already exists, it overrites it
    and if it doesn't exist, it creates it. The function also
    returns the number of characters written
    """
    with open(filename, "w") as file:
        characters = file.write(text)
        return characters
