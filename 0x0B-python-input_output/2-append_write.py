#!/usr/bin/python3

"""
Append a file
"""


def append_write(filename="", text=""):
    """
    Append a file
    """
    with open(filename, 'a') as f:
        return f.write(text)
