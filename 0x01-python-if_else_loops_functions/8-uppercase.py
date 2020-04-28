#!/usr/bin/python3
def uppercase(str):
    result = ''
    for char in range(len(str)):
        if ord(str[char]) >= 97 and ord(str[char]) <= 122:
            result += chr(ord(str[char]) - 32)
        else:
            result += chr(ord(str[char]))
    print("{:s}".format(result))
