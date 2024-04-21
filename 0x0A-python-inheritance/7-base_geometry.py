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

    def integer_validator(self, name, value):
        """
        Public instance method that validates value
        :param name:
        :param value:
        :return: None
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
