#!/bin/bash
#  a Bash script that takes in a URL, sends a request to that URL,
curl -s -I "$arg" | grep -i "^Content-Length:" | cut -d' ' -f2
