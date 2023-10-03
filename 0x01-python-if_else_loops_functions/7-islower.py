#!/usr/bin/env python3

import sys

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./7-islower.py <character>")
    character = sys.argv[1]
    print("Character '{}' is {}".format(character, "lower" if islower(character) else "upper"))
