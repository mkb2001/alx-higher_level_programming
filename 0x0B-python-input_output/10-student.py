#!/usr/bin/python3

"""
Student to JSON
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of Student object
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """

        if attrs is None:
            return self.__dict__
        else:
            dict = {}
            for key in attrs:
                if hasattr(self, key):
                    dict[key] = getattr(self, key)
            return dict
