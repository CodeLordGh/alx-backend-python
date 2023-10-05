#!/bin/bas/env python3
"""
 duck type an iterable object
"""

from typing import Iterable, List, Tuple, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    return the lengh
    """
    return[(i, len(i)) for i in lst]
