#!/usr/bin/python3
"""
Module for add_attribute function.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Raises a TypeError exception if it's not possible.

    Args:
    - obj (object): object to add the attribute to
    - attr (str): attribute name
    - value (any): attribute value
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
