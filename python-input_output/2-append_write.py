#!/usr/bin/python3
"""Append to a file"""
def append_write(filename="", text=""):
    with open(filename, "a+") as file:
        return(file.write(text))
