#!/usr/bin/python3

alphabet = ""
for i in range(ord('a'), ord('z') + 1):
    alphabet += "{}".format(chr(i))

print(alphabet, end='')
