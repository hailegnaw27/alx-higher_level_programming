#!/usr/bin/python3

"""
This module defines the Square class.
"""

class Square:
    """
    This class represents a square.
    """

    def __init__(self, size):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
