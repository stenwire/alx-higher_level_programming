#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


from wsgiref import headers


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    url = 'https://api.github.com/users/'
    name = sys.argv[1]
    pwd = sys.argv[2]
    headers = {'Authorization': 'token %s' %pwd}
    params = {'username':pwd}
    print(headers)
    req = requests.get(f'{url}{name}auth={HTTPBasicAuth(name, pwd)}')
    print(req.headers.get('id'))
