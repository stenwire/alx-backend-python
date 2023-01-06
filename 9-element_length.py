#!/usr/bin/env python3
"""
This is part of 0x00-python_variable_annotations
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Accepts a list and returns a tuple of the items and its length

    Args:
        lst: iterable list

    Return:
        tuple, list, int
    """
    return [(i, len(i)) for i in lst]
