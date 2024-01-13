#!/usr/bin/python3
"""
This is a unittest case in the subdirectory 'tests' this
"""


import unittest
max_int = __import__("6-max_integer").max_integer


class funcTest(unittest.TestCase):
    """
    A class is being declared in order to be able to run a
    unittest case, and the class inherits the unittest.TestCase
    function
    """

    def test_isNon(self):
        self.assertIsNone(max_int([]))

    def test_isNotNone(self):
        self.assertIsNotNone(max_int([1, 2, 3, 4, 5, 6, 7]))

    def test_highestInt(self):
        Highest = max_int([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(Highest, 8)

    def test_IsAnInt(self):
        dataType = max_int([1, 76, 4, 6])
        self.assertTrue(type(dataType) == int)
