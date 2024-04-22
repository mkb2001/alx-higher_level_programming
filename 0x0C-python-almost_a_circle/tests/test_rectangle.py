#!/usr/bin/python3
"""Unittest for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Test cases for rectangle.py"""

    def test_init(self):
        """Test constructor"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)
        self.assertEqual(r2.id, 5)

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r2.area(), 20)

    def test_str(self):
        """Test __str__ method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(str(r1), '[Rectangle] (1) 0/0 - 10/2')
        r2 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(str(r2), '[Rectangle] (5) 3/4 - 10/2')

    def test_display(self):
        """Test display method"""
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.display(), None)
        r2 = Rectangle(2, 2, 2, 2)
        self.assertEqual(r2.display(), None)

    def test_update(self):
        """Test update method"""
        r1 = Rectangle(10, 2)
        r1.update(89)
        self.assertEqual(str(r1), '[Rectangle] (89) 0/0 - 10/2')
        r1.update(89, 2)
        self.assertEqual(str(r1), '[Rectangle] (89) 0/0 - 2/2')
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), '[Rectangle] (89) 3/0 - 2/2')
        r1.update(89, 2, 3, 4)
        self.assertEqual

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.to_dictionary(), {'id': 1, 'width': 10, 'height': 2, 'x': 0, 'y': 0})
        r2 = Rectangle(10, 2, 3, 4, 5)
        self.assertEqual(r2.to_dictionary(), {'id': 5, 'width': 10, 'height': 2, 'x': 3, 'y': 4})
