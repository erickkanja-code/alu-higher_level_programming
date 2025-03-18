#!/usr/bin/python3
"""Same class or inherited fromanother class"""

def is_kind_of_class(obj, a_class):
    """functions that either returns True or False"""
    if isinstance(obj, a_class):
        return "True"
    else:
        return "False"
