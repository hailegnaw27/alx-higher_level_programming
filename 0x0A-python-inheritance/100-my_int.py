#!/usr/bin/python3
"""
Module for MyInt class.
"""


class MyInt(int):
    """
    Class MyInt.

    Attributes:
    - value (int): integer value
    """

    def __eq__(self, other) -> bool:
        """
        Overrides the == operator to test inequality

        Args:
        - other (object): the other object to compare to this instance

        Returns:
        - True if other is not equal to this instance's value, False otherwise
        """
        return int(self) != other

    def __ne__(self, other) -> bool:
        """
        Overrides the != operator to test equality

        Args:
        - other (object): the other object to compare to this instance

        Returns:
        - True if other is equal to this instance's value, False otherwise
        """
        return int(self) == other
