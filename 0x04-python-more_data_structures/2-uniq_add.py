#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    list_set = list(set(my_list)) 
    for x in list_set:
        add += x
    return add
