#!usr/bin/env python
#! -*- coding: utf-8 -*-
"""Task_05"""


def flip_keys(to_flip):
    """This functon reverse nested list items.

        Args:
            to_flip(mixed): arg to be counted and used to loop.
        Returns:
            mixed: reversed list items.
        Examles:
            >>>LIST = [(1, 2, 3), 'abc']
            >>>NEW = flip_keys(LIST)
            >>>LIST is NES
            True
            >>>print LIST
            [(3, 2, 1), 'cba']
     """
    pos = 0
    for pos in range(len(to_flip)):
        item = to_flip[pos]
        pos1 = 0
        for pos1 in range(len(item)):
            item = item[::-1]
            pos1 += 1
        to_flip[pos] = item
        pos += 1
    return to_flip
