#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    res = requests.get('https://alx-intranet.hbtn.io/status')

    content = res.text
    ty = type(content)
    print(f'Body response:\n\t- type: {ty}\n\t- content: {content}')
