#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    req = requests.post(url, data={'email': email})

    print(req.text)
