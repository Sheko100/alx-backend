#!/usr/bin/env python3
"""Module that defines class LRUCache
"""
BaseCache = __import__('base_caching').BaseCaching


class LRUCache(BaseCache):
    """Implements a least recently used cache behavior"""

    def __init__(self):
        """Initialzes the instance"""
        super().__init__()
        self.keys_index = {}
        self.index = 0
        self.lru_index = 0

    def put(self, key, item):
        """Adds an item to the cache and replaces the least recently used item
        if the cache is overload

        Args:
            key: the key of the item
            item: the value that will be associated with the key
        """
        if key is None or item is None:
            return

        if (key not in self.keys_index.values() and
                len(self.cache_data) == super().MAX_ITEMS):
            lru_key = self.keys_index[self.lru_index]
            del self.keys_index[self.lru_index]
            del self.cache_data[lru_key]
            print('DISCARD: {}'.format(lru_key))
            while self.lru_index not in self.keys_index.keys():
                self.lru_index += 1
        elif key in self.keys_index.values():
            del_index = [i for i, k in self.keys_index.items() if k == key][0]
            del self.keys_index[del_index]

        self.keys_index[self.index] = key
        self.index += 1
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item by key

        Args:
            key: key to get the item
        """
        cache = self.cache_data
        value = None

        if key and key in cache:
            value = cache[key]

        return value
