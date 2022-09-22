#!/usr/bin/env bash

arg=$1

curl -s -I "$arg" | grep -i "^content-length:"
