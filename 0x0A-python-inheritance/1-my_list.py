#!/usr/bin/python3
"""
This module contains a class MyList that is a sub-class of the list class.
"""


class MyList(list):
    """
    A sub-class of the built-in list class
    """

    def print_sorted(self):
        """
        Prints a sorted instance of `MyList`
        """
        print(sorted(self))
