#!/usr/bin/python3
def print_list_integer(my_list=[]):
        _len = len(my_list)
        i = 0
        while i < _len:
                print("{:d}".format(my_list[i]))
                i+=1
