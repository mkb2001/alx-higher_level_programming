#!/usr/bin/python3
"""Unittest for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for base.py"""

    def test_id(self):
        """Test id attribute"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(type(file.read()), str)

        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 0, 0, 2)
        Square.save_to_file([s1, s2])
        with open('Square.json', 'r') as file:
            self.assertEqual(type(file.read()), str)

    def test_from_json_string(self):
        """Test from_json_string method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        json_list_dicts = Base.to_json_string(list_dicts)
        new_list_dicts = Base.from_json_string(json_list_dicts)
        self.assertEqual(type(new_list_dicts), list)

        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 0, 0, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        json_list_dicts = Base.to_json_string(list_dicts)
        new_list_dicts = Base.from_json_string(json_list_dicts)
        self.assertEqual(type(new_list_dicts), list)

    def test_create(self):
        """Test create method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)
        self.assertNotEqual(r1_dict, r2.to_dictionary())

        s1 = Square(10, 2, 8, 1)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertNotEqual(s1, s2)
        self.assertNotEqual(s1_dict, s2.to_dictionary())

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles), list)

        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 0, 0, 2)
        Square.save_to_file([s1, s2])
        list_squares = Square.load_from_file()
        self.assertEqual(type(list_squares), list)

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file_csv([r1, r2])
        with open('Rectangle.csv', 'r') as file:
            self.assertEqual(type(file.read()), str)

        s1 = Square(10, 2, 8, 1)
        s2 = Square(2, 0, 0, 2)
        Square.save_to_file_csv([s1, s2])
        with open('Square.csv', 'r') as file:
            self.assertEqual(type(file.read()), str)
