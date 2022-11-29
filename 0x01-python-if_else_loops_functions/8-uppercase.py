#!/usr/bin/python3
def toupper(char):
    if ord(char) >= 96 and ord(char) <= 122:
        return (ord(char) -32)
    else:
        return ord(char)

def uppercase(str):
    str_new = ""
    for char in str:
        str_new += "%c" % toupper(char)
    print("{:s}".format(str_new))
