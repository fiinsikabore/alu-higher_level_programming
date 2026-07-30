#!/bin/bash
# Sends a JSON POST request with contents of a file passed as 2nd argument
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
