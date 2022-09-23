#!/usr/bin/env bash
#  a Bash script that takes in a URL and
# displays all HTTP methods the server will accept

arg=$1
curl -s -I "$arg" | grep -i "^Allow:" 
# curl -sI "$arg" | grep "Allow:" | sed -ne 's/^Allow: //p'