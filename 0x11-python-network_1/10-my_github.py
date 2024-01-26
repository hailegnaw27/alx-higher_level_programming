#!/usr/bin/python3
"""
Module for using the GitHub API to display your GitHub id
"""

import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        json_obj = response.json()
        print(json_obj.get('id'))
    else:
        print("None")

