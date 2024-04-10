#!/usr/bin/python3
"""This is a module representation of a rectangle i Python"""


class Rectangle:
    """This is a class representation of a rectangle i Python"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

                Args:
                    width (int): The width of the new rectangle.
                    height (int): The height of the new rectangle.
        """
        # if type(width) is not int or type(height) is not int:
        #     # if not isinstance(width, int) or not isinstance(height, int):
        #     raise TypeError("width must be an integer")
        # if width < 0 or height < 0:
        #     raise ValueError("width must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""

        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not type(self.__width):
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
        if type(value) is not type(self.__height):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
