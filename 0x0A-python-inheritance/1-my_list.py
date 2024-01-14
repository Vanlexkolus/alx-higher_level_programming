#!/usr/bin/python3
"""
This module is of a class MyList that inherits
'list'
"""


class MyList(list):
    """
    This is a class that inherits a built-in
    class name 'list' and has different methods
    """
    def print_sorted(self):
        """
        This method uses the 'sorted' function present
        in the inherited class 'list' to sort the ints
        from lowest to highest
        """
        sorted_list = sorted(self)
        print(sorted_list)
