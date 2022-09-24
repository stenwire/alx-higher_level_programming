#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        html = res.read()
        ty = type(html)
        enc = html.decode('utf-8')
        str1 = f'- type: {ty}'
        str2 = f'- content: {html}\n\t- utf8 content: {enc}'
        print(f'Body response:\n\t{str1}\n\t{str2}')
