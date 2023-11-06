#!/usr/bin/python3
ass MyList(list):
    """
    Inherits from the list class and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-my_list.txt")
