#!/usr/bin/python3
"""This module prints out the contents of a file to stdout"""
def read_file(filename=""):
    with open(f"{filename}", "r") as file:
        print(file.read(), end="")
