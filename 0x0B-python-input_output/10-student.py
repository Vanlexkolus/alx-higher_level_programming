#!/usr/bin/python3
"""
This Model is of a class Student that defines a student by:
(based on 9-student.py)
"""


class Student:
    """
    This is the class that that contains
    different methods and attributes of a student
    """

    def __init__(self, first_name, last_name, age):
        """
        propetly setting the attributes and ensuring that the
        value of the attribute is converted to a teh proper data type
        before being assigned to the self.attribute
        """

        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.age = int(age)

    def to_json(self, attrs=None):
        """
        This method returns the dictionary representation of the
        attributes in the class and also includes their attibute type
        """

        if attrs is None or not isinstance(attrs, list):
           return self.__dict__
        return {attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)}
