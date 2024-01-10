#!/usr/bin/python3
"""
This is a function that returns the JSON representation
of an object (string)
"""
import json


def to_json_string(my_obj):
    """
    this function takes in a single argument and returns
    it as a JSON rep of a string
    """
    JsFile = json.dumps(my_obj)
    return JsFile
