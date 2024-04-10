#!/usr/bin/python3
"""This is a module representation of a rectangle i Python"""


class Rectangle:
    """This is a class representation of a rectangle i Python"""

    def __init__(self, width=0, height=0):
        if not isinstance(width, int) or not isinstance(height, int):
            raise TypeError("width must be an integer")
        if width < 0 or height < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
