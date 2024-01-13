#!/usr/bin/python3
import unittest
max_int = __import__ ("6-max_integer").max_integer

class funcTest(unittest.TestCase):

    def test_isNon(self):
        self.assertIsNone(max_int([]))
    
    def test_isNotNone(self):
        self.assertIsNotNone(max_int([1, 2, 3, 4, 5, 6, 7]))
    
    def test_highestInt(self):
        Highest = max_int([1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(Highest, 8)
