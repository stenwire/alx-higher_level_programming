#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    res = requests.get(url)

    req_id = res.headers.get('X-Request-Id')
    print(req_id)
