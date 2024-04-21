#!/usr/bin/python3
"""
A module that checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or an instance of a class that inherited from the specified class
    :param obj:
    :param a_class:
    :return:
    """
    return isinstance(obj, a_class)
