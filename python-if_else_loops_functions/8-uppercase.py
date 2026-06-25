#!/usr/bin/python3
def uppercase(str):
    """Print a string in UPPERCASE"""
    for i in range(len(str)):
        c = str[i]
        if ord('a') <= ord(c) <= ord('z'):
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print(c, end="")
    print("")
