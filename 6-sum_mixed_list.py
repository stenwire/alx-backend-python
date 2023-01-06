#!/usr/bin/env python3
"""
This is part of 0x00-python_variable_annotations
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Accepts a variable and returns a float

    Args:
        mxd_lst: int, float

    Return:
        float
    """
    count = [i for i in mxd_lst]
    return sum(count)
