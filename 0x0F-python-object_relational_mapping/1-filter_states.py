#!/usr/bin/python3
"""
This is a generic text, will uodate
later
"""


import MySQLdb
from sys import argv


def main():
    """
    This is a generic text, will uodate
    later
    """
    MY_HOST = 'localhost'
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]
    MY_PORT = 3306

    db = MySQLdb.connect(
        host=MY_HOST, user=MY_USER,
        passwd=MY_PASS, db=MY_DB, port=MY_PORT)

    cur = db.cursor()
    cur.execute("select * from states where name like binary 'N%';")

    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == '__main__':
    main()