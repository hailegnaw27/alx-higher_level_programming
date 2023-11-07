#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file"""

import json
import os.path
import sys

filename = 'add_item.json'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        json_list = json.load(f)
else:
    json_list = []

for arg in sys.argv[1:]:
    json_list.append(arg)

with open(filename, mode='w') as f:
    json.dump(json_list, f)
