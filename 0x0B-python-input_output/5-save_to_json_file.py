#!/usr/bin/python3
"""
This is a function that writes a JSON obj file into
a txt file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    This method takes in two argument, one is the var of the JSON obj (string)
    while the other is the txt file
    """
    if isinstance(filename, str):
        with open(filename, "w") as txtFile:
            jsonFile = json.dumps(my_obj)
            New = txtFile.write(jsonFile)
