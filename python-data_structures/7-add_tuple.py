#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = tuple_a[:2] + (0, 0)
    b1, b2 = tuple_b[:2] + (0, 0)
    return ((a1+b1), (a2+b2))

