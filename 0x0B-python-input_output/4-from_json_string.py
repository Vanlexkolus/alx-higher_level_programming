#!/usr/bin/python3
"""
This is a function that converts a JSON file into
a python file
"""
import json


def from_json_string(my_str):
    """
    This method takes in a single argument which is the
    JSON string variable
    """
    pyfile = json.loads(my_str)
    return pyfile
