#!/usr/bin/python3
"""
This is a class 'Student' that defines a student by the following:

    Public instance attributes:
        first_name
        last_name
        age
"""


class Student:
    """
    This class defines a student by the following
    listed above
    """

    def __init__(self, first_name, last_name, age):
        """
        making sure all the args are stored in the right format no matter
        what happens
        """

        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.age = int(age)

    def to_json(self):
        """
        This is the funtion that returns
        the dictonary type of the input
        """

        return self.__dict__
