#!/usr/bin/python3
alphabet = 122
while alphabet >= 97:
    if alphabet % 2 == 0:
        print("{:c}".format(alphabet), end='')
        alphabet -= 1
    else:
        print("{:c}".format(alphabet - 32), end='')
        alphabet -= 1
