#!/data/data/com.termux/files/usr/bin/env python3
"""least recently used cache"""
BaseCaching = __import__("base_caching").BaseCaching
from collections import deque


class LRUCache(BaseCaching):
    """class LRUCache is a caching system"""
    def __init__(self):
        super().__init__()
        self.queue = deque()

    def put(self, key, item):
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif self.is_full():
                self.discard_t()
        self.queue.append(key)
        self.cache_data[key] = item
    def get(self, key):
        """returns the item in the self.cache_data linked to the key"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
    def is_full(self):
        """returns true if the cache is full"""
        return self.cache_data.__len__() >= super().MAX_ITEMS
    def discard_t(self):
        """prints the key discarded"""
        popped = self.queue.popleft()
        del self.cache_data[popped]
        print("DISCARD: " + str(popped))
