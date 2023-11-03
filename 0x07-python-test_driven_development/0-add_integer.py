#!/usr/bin/python3
"""
This module defines the add_integer function
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int, float): the first number
        b (int, float): the second number

    Returns:
        int: The sum of a and b

    Raises:
        TypeError: if either of a or b is not an int or a float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
