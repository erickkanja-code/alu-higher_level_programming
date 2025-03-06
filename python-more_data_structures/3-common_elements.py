#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for lang in set_1:
        if lang in set_2:
            new_set.add(lang)
        else:
            continue
    return new_set

