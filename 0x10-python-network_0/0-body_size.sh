#!/bin/bash
# Sends a request to a URL and displays the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
