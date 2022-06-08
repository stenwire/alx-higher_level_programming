#!/usr/bin/python3
def uniq_add(my_list=[]):
    j = 0
    for i in range(0, len(my_list)):
        if my_list[j] in my_list[my_list[j]:]:
            my_list.pop(j)
    return sum(my_list)
