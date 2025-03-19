#!/usr/bin/python3
"""Append to a file"""
def append_write(filename="", text=""):
    """Jack of all trades, master of none!"""
    with open(filename, "a+") as file:
        return(file.write(text))
