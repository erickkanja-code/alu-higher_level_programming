#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:  # Check if the character is lowercase (a-z)
            result += chr(ord(char) - 32)  # Convert to uppercase
        else:
            result += char  # Keep the character unchanged
    print("{}".format(result))  # Print the final uppercase string
