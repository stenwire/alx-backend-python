#!/usr/bin/env python3
"""
This is part of 0x00-python_variable_annotations
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Accepts a variable and returns a float

    Args:
        input_list: list, float

    Return:
        float
    """
    count = [i for i in input_list]
    return sum(count)
