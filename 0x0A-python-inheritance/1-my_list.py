#!/usr/bin/python3
"""
This module is of a class MyList that inherits
from 'list'
"""
from typing import List


class MyList(List):
    """
    This is a class that inherits a built-in
    class name 'list' and has different methods
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
