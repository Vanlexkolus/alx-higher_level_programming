#!/usr/bin/python3

"""
This module contains a class Student that defines a student by:

=> Public instance attributes:
=> first_name
=> last_name
=> age
"""


class Student:
    """
    This is a student class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}

    def reload_from_json(self, json):
        for attr, value in json.items():
            setattr(self, attr, value)
