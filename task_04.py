#!usr/bin/env python
#! -*- coding: utf-8 -*-
"""Task_03"""


def process_data(data):
    """This function does some math.

        Args:
            data(mixed): list or tuple of numbers.

        Returns
            tuple: sum of numbers in list or tuple and it average with floa
        ting point precision.

        Example:
            >>> process_data([1, 2, 3])
            (6, 2.0)"""
    sum_data = 0
    for item in data:
        sum_data = sum_data + item

    average = sum_data / float(len(data))

    return (sum_data, average)
