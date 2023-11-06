#!/usr/bin/python3
"""
This is a module containing the MyList class
which inherits from the list class and has a
method that prints a sorted list.
"""


class MyList(list):
    """
    A class inheriting from the list class

    Methods:
        print_sorted(self)
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList([1, 2, 3, 5, 4, 6, 7, 9])
    print(my_list)
    my_list.print_sorted()
