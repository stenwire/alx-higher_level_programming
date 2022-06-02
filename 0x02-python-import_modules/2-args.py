#!/usr/bin/python3
if __name__ =="__main__":
    from sys import argv

    list = argv
    len = len(argv) - 1
    count = 1

    if len == 0:
            print("{:d} arguements.".format(len))
    elif len == 1:
            print("{:d} arguement:".format(len))
    else:
        print("{:d} arguements:".format(len))

    while count < len or count == len:
        arg = list[count]
        print("{:d}: {:s}".format(count, arg))
        count += 1
