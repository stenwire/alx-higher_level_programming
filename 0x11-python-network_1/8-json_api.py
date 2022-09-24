#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        letter = ""
        res = requests.post(url, data={'q': letter})
    else:
        letter = sys.argv[1]
        res = requests.post(url, data={'q': letter})

    try:
        res = res.json()
        if len(res) < 1:
            print('No result')
        print(f'[{res.get(id)}] {res.get(name)}')
    except Exception:
        print('Not a valid JSON')

