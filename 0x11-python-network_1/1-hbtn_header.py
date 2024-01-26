#!/usr/bin/python3
import urllib.request
import sys

url = sys.argv[1]

if __name__ == "__main__":
with urllib.request.urlopen(url) as response:
    header = response.getheader('X-Request-Id')

print(header)
