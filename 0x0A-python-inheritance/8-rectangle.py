#!/usr/bin/python3
"""
Module for Rectangle class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle.

    Attributes:
    - __width (int): width of the rectangle
    - __height (int): height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initializer for Rectangle instances.

        Args:
        - width (int): width of the rectangle
        - height (int): height of the rectangle
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns the following rectangle description: [Rectangle] <width>/<height>
        """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self) -> int:
        """
        Implements area() method of BaseGeometry class.

        Returns:
        - area of this rectangle instance (__width * __height)
        """
        return self.__width * self.__height
