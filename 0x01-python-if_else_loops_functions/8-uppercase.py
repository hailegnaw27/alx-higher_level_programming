#!/usr/bin/python3

def uppercase(str):
    """
    Prints a string in uppercase.
    """
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        result += uppercase_char

    print(result, end="\n")
