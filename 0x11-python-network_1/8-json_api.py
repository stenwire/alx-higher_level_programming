#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) == 2:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        r_j = r.json()
        id = r_j.get('id')
        name = r_j.get('name')
        if len(r_j) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
