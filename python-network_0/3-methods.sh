#!/bin/bash
# Displays all HTTP methods the server will accept
curl -siX OPTIONS "$1" | grep -i "^Allow:" | cut -d ' ' -f2-
