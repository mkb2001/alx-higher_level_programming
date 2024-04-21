#!/usr/bin/python3
"""
A module that checks if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from the specified class
    :param obj:
    :param a_class:
    :return:
    """
    return issubclass(type(obj), a_class) and a_class is not type(obj)
