#!/usr/bin/env bash
#  a Bash script that sends a request to a URL passed as an argument,
# and displays only the status code of the response.
# You are not allowed to use any pipe, redirection, etc.
# You are not allowed to use ; and &&

arg=$1
curl -so /dev/null --write-out "%{http_code}" "$arg"
