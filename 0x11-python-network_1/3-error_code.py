#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import sys
    import urllib.request as request
    import urllib.error as error
    url = sys.argv[1]

    req = request.Request(url)
    try:
        html = request.urlopen(req)
        print(html.read())
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
