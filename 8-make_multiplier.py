#!/usr/bin/env python3
"""
This is part of 0x00-python_variable_annotations
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiply variable by its self and returns a float

    Args:
        multiplier: float

    Return:
        float
    """
    return multiplier * multiplier
