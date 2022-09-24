#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


from wsgiref import headers


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://docs.github.com/en/rest/users'
    name = sys.argv[1]
    pwd = sys.argv[2]
    headers = {'Authorization': pwd}
    params = {'username':pwd}
    print(headers)
    req = requests.get(url, headers=headers, params=params)
    # print(req.status_code)
    print(req.headers.get('id'))