#!/usr/bin/python3
def best_score(a_dictionary):
    highest_value = 0
    for key, value in a_dictionary.items():
        if value > highest_value:
            highest_value = value
        if value == highest_value:
    return key
