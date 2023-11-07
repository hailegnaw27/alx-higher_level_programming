#!/usr/bin/python3
"""
Module for append_write function.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF8) and returns the number of characters added.

    Args:
    - filename (str): file name/path to append to
    - text (str): text to append to file

    Returns:
    - The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
