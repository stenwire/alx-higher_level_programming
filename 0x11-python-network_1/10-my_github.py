#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = 'https://api.github.com/user'
    name = sys.argv[1]
    pwd = sys.argv[2]

    auth = HTTPBasicAuth(name, pwd)
    req = requests.get(url, auth=auth)
    print(req.json().get("id"))
