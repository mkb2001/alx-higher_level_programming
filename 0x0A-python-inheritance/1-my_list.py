#!/usr/bin/python3
"""
This is a module about inheritance
"""


class MyList(list):

    def print_sorted(self):
        """
        Prints the list, but sorted
        """
        print(sorted(self))
