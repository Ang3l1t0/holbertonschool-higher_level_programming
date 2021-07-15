#!/usr/bin/python3
"""text_indentation
"""


def text_indentation(text):
    '''This function prints with indentation.
    - text {str} will be printed with indentations'''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    ar = []
    con = text.count('.')
    con += text.count(':')
    con += text.count('?')
    tripper = 0
    for x in range(con):
        ar.append([])
        for y in range(tripper, len(text)):
            if y == 0:
                y += tripper
            ar[x].append(text[y])
            if text[y] in '.?:':
                tripper = y + 1
                ar[x].append('\n\n')
                break
    for x in range(len(ar)):
        for i in range(len(ar[x])):
            if ar[x][i] == ' ':
                ar[x].pop(i)
            else:
                break

    for x in ar:
        print(*x, sep="", end="")
