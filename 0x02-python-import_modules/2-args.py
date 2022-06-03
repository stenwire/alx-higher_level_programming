#!/usr/bin/python3
if __name__ =="__main__":
    from sys import argv
    list = argv
    len = len(list) - 1
    if len == 0:
            print("{:d} arguements.".format(len))
    elif len == 1:
            print("{:d} arguement:".format(len))
    else:
        print("{:d} arguements:".format(len))
    for i in range(1, len):
        print("{}: {}".format(i, list[i]))
