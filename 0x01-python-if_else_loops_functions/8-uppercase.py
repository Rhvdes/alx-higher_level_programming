#!/usr/bin/python3
def uppercase(string):
    for c in string:
        if ord(c) >= 97 and ord(c) <= 122:
            print(chr(ord(c) - 32), end="")
        else:
            print(c, end="")
    print()
