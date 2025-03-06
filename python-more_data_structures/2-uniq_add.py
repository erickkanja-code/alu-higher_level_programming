#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for num in my_list:
        if num not in new_list:
            new_list.append(num)
        else:
            continue
        sum = 0
    for unique_num in new_list:
        sum += unique_num
    return sum
