#!/usr/bin/python3

def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if ascii_value >= 97 and ascii_value <= 122:
            ascii_value -= 32
        print(chr(ascii_value), end="")
    print()

uppercase("best")
uppercase("Best School 98 Battery street")
