#!/usr/bin/python3
"""
Module for sending a POST request with an email parameter to a URL and displaying the response body
"""
import requests
from sys import argv

if __name__ == "__main__":
    print(requests.post(argv[1], data={'email': argv[2]}).text)
