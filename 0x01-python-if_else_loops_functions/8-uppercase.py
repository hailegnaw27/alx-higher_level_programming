#!/usr/bin/python3

def uppercase(str):
    result = ""
    for char in str:
        ascii_value = ord(char)
        if ascii_value >= 97 and ascii_value <= 122:
            ascii_value -= 32
        result += "{}".format(chr(ascii_value))
    print(result)

uppercase("best")
uppercase("Best School 98 Battery street")
