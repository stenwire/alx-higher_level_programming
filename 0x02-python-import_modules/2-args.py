#!/usr/bin/python3
if __name__ =="__main__":
    from sys import argv

    list = argv
    len = len(argv) - 1
    count = 1

    if len == 0:
            print(f"{len:d} arguements.")
    elif len == 1:
            print(f"{len:d} arguement:")
    else:
        print(f"{len:d} arguements:")

    while count < len or count == len:
        arg = list[count]
        print(f"{count:d}: {arg:s}")
        count += 1
