#!/usr/bin/python3
from sys import argv
arguments = argv
sum_of_arguments = 0
for i in arguments[1:]:
    sum_of_arguments += int(i)
print(sum_of_arguments)
