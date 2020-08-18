#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted
integers
"""


def find_peak(list_of_integers):

    if not list_of_integers:
        return None
    lenght = len(list_of_integers)
    if lenght > 1:
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
        half = len(list_of_integers) // 2
        if (half == lenght - 1 or list_of_integers[half] >=
            list_of_integers[half + 1]) and\
            (half == 0 or list_of_integers[half] >=
             list_of_integers[half - 1]):
            return list_of_integers[half]

        elif half != lenght - 1 and\
                (list_of_integers[half + 1] > list_of_integers[half]):
            return find_peak(list_of_integers[half + 1:])
        return find_peak(list_of_integers[:half])
