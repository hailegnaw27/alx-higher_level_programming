#!/bin/bash
# Sends a GET request to a URL and displays the body of the response
curl -sL -w "%{http_code}" -o /dev/null "$1" -X GET -H "Content-Type: application/json" | grep -q "200" && curl -sL "$1"
