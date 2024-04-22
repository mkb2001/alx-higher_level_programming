#!/usr/bin/python3

"""Unittest for square.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Test cases for square.py """

    def test_init(self):
        """ Test constructor """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        s2 = Square(5, 3, 4, 5)
        self.assertEqual(s2.size, 5)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)
        self.assertEqual(s2.id, 5)

    def test_str(self):
        """ Test __str__ method """
        s1 = Square(5)
        self.assertEqual(str(s1), '[Square] (1) 0/0 - 5')
        s2 = Square(5, 3, 4, 5)
        self.assertEqual(str(s2), '[Square] (5) 3/4 - 5')

    def test_size(self):
        """ Test size getter and setter """
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(s1.size, 10)

    def test_update(self):
        """ Test update method """

        s1 = Square(5)
        s1.update(89)
        self.assertEqual(str(s1), '[Square] (89) 0/0 - 5')
        s1.update(89, 2)
        self.assertEqual(str(s1), '[Square] (89) 0/0 - 2')
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), '[Square] (89) 3/0 - 2')
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), '[Square] (89) 3/4 - 2')

    def test_to_dictionary(self):
        """ Test to_dictionary method """

        s1 = Square(5)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 5, 'x': 0, 'y': 0})
        s2 = Square(5, 3, 4, 5)
        self.assertEqual(s2.to_dictionary(), {'id': 5, 'size': 5, 'x': 3, 'y': 4})
