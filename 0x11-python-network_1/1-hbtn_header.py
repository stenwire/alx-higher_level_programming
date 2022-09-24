#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import sys
    import urllib.request as request
    ur_l = sys.argv[1]
    with request.urlopen(ur_l) as res:
        req_id = res.headers.get('X-Request-Id')

    print(req_id)
