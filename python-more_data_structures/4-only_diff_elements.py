#!/usr/bin/python 3
def only_diff_elements(set_1, set_2):
    new_set = set()
    for lang in set_1:
        if lang not in set_2:
            new_set.add(lang)
        else:
            continue
    for lang2 in set_2:
        if lang2 not in new_set and lang2 not in set_1:
            new_set.add(lang2)
    return new_set
