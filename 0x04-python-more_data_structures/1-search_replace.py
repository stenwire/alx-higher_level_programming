#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(map((lambda x: x), my_list))
    for i in range(len(new_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
    return new_list
