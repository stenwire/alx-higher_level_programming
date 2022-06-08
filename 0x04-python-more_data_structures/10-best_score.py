#!/usr/bin/python3
def best_score(a_dictionary):
    my_list = []
    if a_dictionary:
        for val in a_dictionary.values():
            my_list.append(val)
        max = my_list[0]
        for i in range(0, len(my_list)):
            if(my_list[i] > max):
                max = my_list[i]
        for key in a_dictionary.keys():
            key_val = max
            if a_dictionary[key] == key_val:
                return key
    else:
        return None
