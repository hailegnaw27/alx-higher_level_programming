#!/usr/bin/python3
"""
Module for load_from_json_file function.
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
    - filename: name of JSON file to read

    Returns:
    - The corresponding Python object.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
