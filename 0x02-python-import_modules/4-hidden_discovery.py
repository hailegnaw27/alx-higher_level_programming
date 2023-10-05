#!/usr/bin/python3
import dis

def print_names():
    names = dir(hidden_4)
    sorted_names = sorted(names)
    for name in sorted_names:
        if not name.startswith('__'):
            print(name)

# Importing the module
import hidden_4

# Disassembling the module
dis.dis(hidden_4)

# Printing the names
print_names()

