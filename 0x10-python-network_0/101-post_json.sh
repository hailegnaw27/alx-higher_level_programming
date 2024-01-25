#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response

# Check if the file exists
if [ ! -f "$2" ]; then
    echo "File does not exist."
    exit 1
fi

# Check if the file contains valid JSON
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send the POST request and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
