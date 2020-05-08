#!/usr/bin/python3
def roman_to_int(roman_string):
    rn = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000
        }
    res = 0
    for i in range(0, len(roman_string)):
        if i == 0 or rn[roman_string[i]] <= rn[roman_string[i - 1]]:
            res += rn[roman_string[i]]
        else:
            res += rn[roman_string[i]] - 2 * rn[roman_string[i - 1]]
    return res
