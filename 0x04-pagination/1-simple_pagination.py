#!/data/data/com.termux/files/usr/bin/env python3
"""Implement a method named get_page that takes two integer
arguments page with default value 1 and page_size with default value 10
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int):
    return ((page - 1) * page_size, page * page_size)

class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from csv dataset"""
        try:
            assert page > 0
            assert page_size > 0
        except Exception as e:
            raise AssertionError

        dataset = self.dataset()

        if page > len(dataset) or page_size > len(dataset):
            return []
        indexes = index_range(page, page_size)
        return dataset[indexes[0]:indexes[1]]
