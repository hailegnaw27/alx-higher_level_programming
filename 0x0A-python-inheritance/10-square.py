#!/usr/bin/python3
"""
Module for Square class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square.

    Attributes:
    - __size (int): size of the square
    """

    def __init__(self, size):
        """
        Initializer for Square instances.

        Args:
        - size (int): size of the square
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the following square description: [Square] <size>/<size>
        """
        return '[Square] {}/{}'.format(self.__size, self.__size)

    def area(self) -> int:
        """
        Implements area() method of Rectangle class.

        Returns:
        - area of this square instance (__size * __size)
        """
        return self.__size ** 2
