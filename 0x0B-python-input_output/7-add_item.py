#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""


class BaseGeometry:
    """
    Class BaseGeometry.
    """

    def area(self):
        """
        Public instance method: area()

        Raises:
        Exception: when area is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Public instance method: integer_validator(name, value)

        Args:
        - name (str): name of variable
        - value (int): integer to validate

        Raises:
        TypeError: if value is not an integer
        ValueError: if value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
