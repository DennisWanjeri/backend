#!/data/data/com.termux/files/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """paginates a database containing popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"


    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """cached dataset"""
        if self.__dataset == None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset
    def indexed_dataset(self) -> Dict[int, List]:
        """dataset indexed by sorting position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
                }
        return self.__indexed_dataset
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Deletion-resilient hypermedia pagination"""
        _dataset = self.indexed_dataset()
        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": page_size,
            "data": [_dataset.get(index + i) for i in range(page_size)]
            }
