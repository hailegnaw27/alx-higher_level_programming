#!/usr/bin/python3
"""
Script for adding arguments to a list and saving them to a file.
"""
import sys
from os import path
from typing import List
from json import dumps
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


def add_item(filename: str, item_list: List[str]) -> None:
    """
    Adds all items in item_list to a list loaded from filename, and saves
    the resulting list back to filename as a JSON representation.

    If filename does not exist, a new list is created and saved to filename.

    Args:
    - filename: name of file to read from/write to
    - item_list: list of strings to add to the list

    Returns:
    - Nothing.
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(item_list)
    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    filename = "add_item.json"
    item_list = sys.argv[1:]
    add_item(filename, item_list)
