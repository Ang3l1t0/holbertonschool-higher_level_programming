#!/usr/bin/python3
def weight_average(my_list=[]):
    div = 0
    res = 0
    if not my_list:
        return 0
    for i in range(0, len(my_list)):
        res = res + my_list[i][0] * my_list[i][1]
        div = div + my_list[i][1]
    return res / div
