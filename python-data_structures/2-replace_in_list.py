#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    for num in my_list:
        if idx > (len(my_list) - 1):
            return my_list
        elif idx < 0:
            return my_list
        else:
            my_list[3] = element
            return my_list
