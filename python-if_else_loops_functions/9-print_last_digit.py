#!/usr/bin/python3
def print_last_digit(number):
    num_list = list(str(number))
    num = int(num_list[-1])
    print(num, end='')
    return num
