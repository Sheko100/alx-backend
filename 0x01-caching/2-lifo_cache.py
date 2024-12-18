#!/usr/bin/env python3
"""Module that defines FIFOCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Creates a cache with last in first out mechanism
    """

    def put(self, key, item):
        """Inserts an item to the cache
        and discards the last inserted item
        """
        if key and item:
            limit = self.MAX_ITEMS
            cache = self.cache_data
            cache_len = len(cache)

            if cache_len == limit and key not in cache:
                self.cache_data.pop(self.last_key)
                print("DISCARD:", self.last_key)

            self.last_key = key
            self.cache_data[key] = item

    def get(self, key):
        """gets an item from the cache based on the key
        """
        if key and key in self.cache_data:
            return self.cache_data[key]

        return None
