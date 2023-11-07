#!/usr/bin/python3
"""
Module for from_json_string function.
"""
import json


def from_json_string(my_str):
    """
    Takes a JSON string and returns its corresponding object.

    Args:
    - my_str (str): JSON string to convert to object

    Returns:
    - The corresponding Python object.
    """
    return json.loads(my_str)
