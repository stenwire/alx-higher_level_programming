#!/bin/bash
#  a Bash script that takes in a URL and
curl -s -I "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
