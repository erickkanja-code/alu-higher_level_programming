#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        highest_no = 0
        for num in my_list:
            if num > highest_no:
                highest_no = num
            else:
                highest_no = highest_no
    return highest_no
