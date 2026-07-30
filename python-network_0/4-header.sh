#!/bin/bash
# Sends a GET request with custom header x-HolbertonSchool-User-Id: 98
curl -sH "x-HolbertonSchool-User-Id: 98" "$1"
