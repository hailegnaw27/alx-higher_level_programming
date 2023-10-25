#!/usr/bin/python3
"""
This module defines the Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.
        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
