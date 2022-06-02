#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    list = argv
    new_list = list.pop(0)
    count = 0

    for i in range(0, len(list)):
        count += int(list[i])
    print(count)
