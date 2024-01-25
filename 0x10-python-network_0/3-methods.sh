#!/bin/bash
# Displays all HTTP methods accepted by the server for a URL
curl -sI "$1" | grep -i Allow | cut -d ' ' -f 2-
