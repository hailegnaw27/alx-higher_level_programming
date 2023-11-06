#!/usr/bin/python3


class MyList(list):
    """
    MyList class that inherits from list.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
