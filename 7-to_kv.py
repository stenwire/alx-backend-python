#!/usr/bin/env python3
"""
This is part of 0x00-python_variable_annotations
"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Accepts two variables and returns a tuple

    Args:
        k: string
        v: int, float

    Return:
        tuple, str, float
    """
    return (k, v**2)
