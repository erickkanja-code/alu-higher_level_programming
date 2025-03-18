#!/usr/bin/python3
"""Only a sub class of"""

def inherits_from(obj, a_class):
    """You know what, they're paying"""
    return isinstance(obj, a_class) and type(obj) != a_class
