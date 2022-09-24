#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import sys
    from  urllib import request, parse
    url = sys.argv[1]
    email = sys.argv[2]

    body = {'email': email}
    data = parse.urlencode(body)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as res:
        html = res.read()

    print(f'Your email is: {data}')
