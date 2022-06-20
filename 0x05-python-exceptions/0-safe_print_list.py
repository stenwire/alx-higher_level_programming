#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    num_of_elm_to_print = 0
    new_list = ''

    try:
        for item in my_list:
            len += 1

        if x > len:
            num_of_elm_to_print = len
        else:
            num_of_elm_to_print = x

        for i in range(0, num_of_elm_to_print):
            new_list += str(my_list[i])
        print (int(new_list))
        return (num_of_elm_to_print)

    except (NameError, ValueError, SyntaxError):
        print ('An error occured, pls try again!')