#!/data/data/com.termux/files/usr/bin/env python3
"""Write a function named index_range that
takes two integer arguments page and page_size
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Returns a tuple containing a start and end index corresponding to the range of indexes to return in a list for those particular pagination parameters.
    """
    
    if page <= 1:
        return (0, page_size)
    else:
        return ((page * page_size) - page_size, (page * page_size))
