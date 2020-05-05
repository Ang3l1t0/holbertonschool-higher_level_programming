#!/usr/bin/python3
def no_c_prints(s):
    new_string = ' '
    for character in s:
        if character != 'c' and character != 'C':
            new_string += character
    print(new_string)

print(no_c_prints("Characters"))