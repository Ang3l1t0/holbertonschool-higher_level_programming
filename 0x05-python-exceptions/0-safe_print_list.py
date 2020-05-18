#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        printed = 0
        try:
            print(my_list[i], end="")
            printed += 1
        except IndexError:
            pass
    print()
    return (printed)