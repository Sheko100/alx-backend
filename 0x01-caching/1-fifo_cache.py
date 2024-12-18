#!/usr/bin/env python3
"""Module that defines FIFOCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """Creates a cache with first in first out mechanism
    """

    def put(self, key, item):
        """Inserts an item to the cache
        and discards the last inserted item
        """
        if key and item:
            cache = self.cache_data
            limit = BaseCaching.MAX_ITEMS
            cache_len = len(cache)

            if cache_len == limit and key not in cache:
                first_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(first_key)
                print("DISCARD:", first_key)

            self.cache_data[key] = item

    def get(self, key):
        """gets an item from the cache based on the key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]

        return None
