#!/usr/bin/env bash
#  a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response

arg=$1
curl -s -I "$arg" | grep -i "^Content-Length:" | cut -d' ' -f2
