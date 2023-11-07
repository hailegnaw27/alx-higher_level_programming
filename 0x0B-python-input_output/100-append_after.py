#!/usr/bin/python3
"""
Module for append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Args:
        - filename: string containing the name of the file to be modified
        - search_string: string containing the text to search for in each line
        - new_string: string to be inserted after each line containing search_string

    Returns:
        - Nothing.
    """
    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
        f.truncate()
