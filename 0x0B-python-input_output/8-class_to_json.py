#!/usr/bin/python3
"""
Module for class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an instance of a Class.

    Args:
    - obj: an instance of a Class

    Returns:
    - A dictionary containing the attributes of the object.
    """
    return obj.__dict__
