#!/data/data/com.termux/files/usr/bin/env python3
"""LFU caching"""

from enum import Enum
from heapq import heappush, heappop
from itertools import count

BaseCaching = __import__("base_caching").BaseCaching

class HeapItemStatus(Enum):
    """Heap item status, to be implemented using an enum"""
    ACTIVE = 1
    INACTIVE = 2

class LFUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """initialization"""
        super().__init__()
        self.heap = []
        self.map = {}
        self.counter = count()
    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.rehydrate(key)
            else:
                if self.is_full():
                    self.evict()
                self.add_to_heap(key)
            self.cache_data[key] = item


    def get(self, key):
        if key in self.cache_data:
            self.rehydrate(key)
            return self.cache_data.get(key)

    def is_full(self):
        """checks whether cache_data is full"""
        return len(self.cache_data) >= self.MAX_ITEMS
    def evict(self):
        while self.heap:
            _, __, item, status = heappop(self.heap)
            if status == HeapItemStatus.ACTIVE:
                print("DISCARD: " + str(item))
                del self.cache_data[item]
                return

            
    def add_to_heap(self, key, count=0):
        """adds a new entry to a heap"""
        entry = [1 + count, next(self.counter), key, HeapItemStatus.ACTIVE]
        self.map[key] = entry
        heappush(self.heap, entry)

        
    def rehydrate(self, key):
        """marks current item as inactive"""
        entry = self.map[key]
        entry[-1] = HeapItemStatus.INACTIVE
        self.add_to_heap(key, entry[0])
