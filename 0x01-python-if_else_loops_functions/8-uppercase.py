#!/usr/bin/python3

def uppercase(str):
    """
    Prints a string in uppercase.
    """
    for char in str:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122:
            ascii_val -= 32
        print(chr(ascii_val), end="")
    print()
