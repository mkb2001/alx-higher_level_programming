#!/usr/bin/python3
"""
A module that defines a function that adds an attribute to an object if possible
"""


def add_attribute(attribute, value):
    """
    A function that adds an attribute to an object if possible
    :param attribute: attribute to add
    :param value: value of the attribute
    :return: None
    """
    if hasattr(attribute, '__dict__'):
        setattr(attribute, value, value)
    else:
        raise TypeError("can't add new attribute")
