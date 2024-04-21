#!/usr/bin/python3
"""
A module that defines a class BaseGeometry

"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """
        Public instance method that raises an Exception with the message area() is not implemented
        :return: None
        """
        raise Exception("area() is not implemented")
