#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map((lambda x: x), my_list))
    for i in range(0, len(new_list)-1):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
