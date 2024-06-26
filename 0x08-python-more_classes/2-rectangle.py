#!/usr/bin/python3
"""This is a module representation of a rectangle in Python"""


class Rectangle:
    """This is a class representation of a rectangle i Python"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

                Args:
                    width (int): The width of the new rectangle.
                    height (int): The height of the new rectangle.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
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
        """Get/set the height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
