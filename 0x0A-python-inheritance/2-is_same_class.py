#!/usr/bin/python3
"""
A module that checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a class
    :param obj:
    :param a_class:
    :return:
    """
    return type(obj) == a_class
