#!/data/data/com.termux/files/usr/bin/env python3
"""Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic caching"""
    def put(self, key, item):
        """add data to a caching system"""
        if key is None or item is None:
            pass
        else:
            self.cache_data.update({key: item})
    def get(self, key):
        """Retreive data from a cache"""
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
