#!/usr/bin/env bash
# A Bash script that sends a JSON POST request to a URL passed as the first argument
# and displays only the status code of the response.

arg1=$1
arg2=$2
curl -s -X POST -H "Content-Type: application/json" -d @"$arg2" "$arg1"
