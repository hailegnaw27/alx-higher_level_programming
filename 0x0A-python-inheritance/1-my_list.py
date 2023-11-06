#!/usr/bin/python3
"""
Module: `1-my_list.py`
"""


class MyList(list):
    """
    Class MyList that inherits from list

    Methods:
        print_sorted(self): prints the list, but sorted (ascending order)
    """

    def print_sorted(self):
        """
        Prints the list of integers in ascending sorted order
        """
        print(sorted(self))
