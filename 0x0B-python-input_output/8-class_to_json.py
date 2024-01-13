#!/usr/bin/python3
"""
This function returns  dictionary description
for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    obj_dictionary = obj.__dict__

    if hasattr(obj, "__class__"):
        obj_dictionary["__class__"] = obj.__class__.__name__
    for key, value in obj_dictionary.items():
        if hasattr(value, "__dict__"):
            obj_dictionary[key] = value.__dict__
    """
    return obj.__dict__
