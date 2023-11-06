#!/usr/bin/python3

"""
Module: 1-my_list
This module defines the MyList class, which inherits from the list class.

"""

class MyList(list):
    """
    Class MyList
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Public instance method: print_sorted
        Prints the list in ascending order.

        Args:
            None.

        Returns:
            None.

        """
        sorted_list = sorted(self)
        print(sorted_list)

