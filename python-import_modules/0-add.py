#!/usr/bin/python3
"""Imports add from add_0 and prints the result of a + b."""
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
