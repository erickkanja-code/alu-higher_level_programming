#!/usr/bin/python3
import sys
arguments = sys.argv
sum_of_arguments = 0
for i in arguments[1:]:
    sum_of_arguments += int(i)
print(sum_of_arguments)
