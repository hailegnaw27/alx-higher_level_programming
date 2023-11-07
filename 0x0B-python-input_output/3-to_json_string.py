#!/usr/bin/python3
"""
Module for to_json_string function.
"""
import json


def to_json_string(my_obj):
    """
    Takes an object and returns its JSON representation as a string.

    Args:
    - my_obj: object to convert to JSON

    Returns:
    - The JSON string representation of the object.
    """
    return json.dumps(my_obj)
