#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        ascii_value = ord(char)
        if ascii_value >= 97 and ascii_value <= 122:
            ascii_value -= 32
        result += chr(ascii_value)
    print("{}".format(result))

uppercase("best")
uppercase("Best School 98 Battery street")
uppercase("Holberton School")
uppercase("Holberton School, 98 battery street")
uppercase("98")
uppercase("z")
uppercase("Z")
