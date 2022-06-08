#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common_set = set_1 & set_2
    union_set = set_1.union(set_2)
    new_set = set()
    for item in union_set:
        if item not in common_set:
            new_set.add(item)
    return new_set
