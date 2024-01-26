#!/usr/bin/python3
"""
Module for sending a request to a URL and displaying the body of the response,
or printing an error message if the HTTP status code is greater than or equal to 400
"""
import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
