#!/usr/bin/python3
"""
Module for sending a request to a URL and displaying a specific response header value
"""
import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).headers.get("X-Request-Id"))
