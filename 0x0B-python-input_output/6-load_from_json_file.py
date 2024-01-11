#!/usr/bin/python3
"""
This is a function that creates an Obj (str)
from a JSON file. Basically, it locates, open, and converts
a JSON file into a python file
"""
import json


def load_from_json_file(filename):
    """
    This function takes in one argument
    which is filename. filename is a JSON file and it's
    going to be converted into a python file
    """
    with open(filename, "r") as filepointer:
        read_file = filepointer.read()
        ObjPyFile = json.loads(read_file)
        return ObjPyFile
