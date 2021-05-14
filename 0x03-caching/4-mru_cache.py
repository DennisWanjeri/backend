#!/data/data/com.termux/files/usr/bin/env python3
"""most recently used cache implementation"""

from collections import deque


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.queue = deque()
    def put(self, key, item):
        """if key exists, we update it in our queue, otherwise we add it to reflect most recently used"""
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.evict()
            self.queue.append(key)
            self.cache_data[key] = item
    def get(self, key):
        """returns value in cache_data linked to key"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
    def is_full(self):
        """if number of items in self.cache_data exceeds its capacity"""
        return len(self.cache_data) >= self.MAX_ITEMS
    def evict(self):
        popped = self.queue.pop()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
