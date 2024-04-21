#!/usr/bin/python3
"""
A module that defines a class MyInt
"""


class MyInt(int):
    """
    A class MyInt that inherits from int
    """

    def __eq__(self, other):
        """
        Override the equality operator
        :param other:
        :return:
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator
        :param other:
        :return:
        """
        return super().__eq__(other)
