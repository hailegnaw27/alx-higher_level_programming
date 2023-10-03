#!/usr/bin/python3

for ascii_value in range(122, 96, -1):
    if ascii_value % 2 == 0:
        letter = chr(ascii_value)
    else:
        letter = chr(ascii_value - 32)
    print("{}".format(letter), end="")

print()
