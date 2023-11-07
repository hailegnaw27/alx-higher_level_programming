#!/usr/bin/python3
"""
Module for save_to_json_file function.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
    - my_obj: object to write to file as JSON
    - filename: name of file to write to

    Returns:
    - Nothing.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
