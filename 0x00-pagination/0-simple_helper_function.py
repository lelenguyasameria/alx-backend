#!/usr/bin/env python3
"""a function to help pagination.
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """"retrieves the index range from the a certain given size.
    """

return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)