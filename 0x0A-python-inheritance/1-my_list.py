#!/usr/bin/python3
""" My list
    """


class MyList(list):
    """print_sorted

        Arguments:
            list {list} -- [create a new sorted list]
        """

    def print_sorted(self):
        new_list = []
        new_list = self.copy()
        new_list.sort()
        print(new_list)
