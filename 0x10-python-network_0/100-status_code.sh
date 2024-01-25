#!/bin/bash
# Sends a request to a URL and displays only the status code of the response
curl -s -o /tmp/response.txt -w "%{http_code}" "$1"
cat /tmp/response.txt
