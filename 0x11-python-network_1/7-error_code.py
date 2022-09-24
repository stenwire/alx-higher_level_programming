#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    req = requests.get(url)

    if (req.status_code >= 400):
        print(f'Error code: {req.status_code}')