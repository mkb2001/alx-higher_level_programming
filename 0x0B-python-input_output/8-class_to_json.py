#!/usr/bin/python3

"""
JSON representation of an object
"""


def class_to_json(obj):
    """JSON representation of an object"""
    return obj.__dict__
