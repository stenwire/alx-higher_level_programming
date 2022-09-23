#!/usr/bin/env bash
# A Bash script that sends a DELETE request
# to the URL passed as the first argument

arg=$1
curl -X "DELETE" -s "$arg"
