#!/usr/bin/python3
""" This class is a Square class"""


class Square:
    """ This is the first method in the class to be run at initialization"""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
