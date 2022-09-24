#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys, json

    url = 'https://developer.github.com/v3/repos/'
    repo = sys.argv[1]
    owner = sys.argv[2]

    # auth = HTTPBasicAuth()

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    req = requests.get(url)
    req = req.json()

    # print(req.json().get('author'))
    for x in req:
        print(x['author'])
