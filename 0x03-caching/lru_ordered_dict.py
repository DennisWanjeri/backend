#!/data/data/com.termux/files/usr/bin/env python3
from collections import OrderedDict
class LRUCache:
    """initializing capacity"""
    def __init__(self, capacity: int):
        """initializing the capacity
        also the cache will be an OrderedDict"""
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key: int) -> int:
        """if key is not present we return -1, otherwise we push the key to the end to keep track of recently used key"""
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

cache = LRUCache(2) 
 
 

cache.put(1, 1)

print(cache.cache)

cache.put(2, 2)

print(cache.cache)

cache.get(1)

print(cache.cache)

cache.put(3, 3)

print(cache.cache)

cache.get(2)

print(cache.cache)

cache.put(4, 4)

print(cache.cache)

cache.get(1)

print(cache.cache)

cache.get(3)

print(cache.cache)

cache.get(4)

print(cache.cache)
