#!/usr/bin/python3
def check(tuple, pos):
    try:
        return (tuple[pos])
    except IndexError:
        return (0)


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = (check(tuple_a, 0) + check(tuple_b, 0))
    tuple_2 = (check(tuple_a, 1) + check(tuple_b, 1))
    return (tuple_1, tuple_2)
