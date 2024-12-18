#!/usr/bin/env python3
"""Module that defines basic_cache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic cache operations
    """

    def put(self, key, item):
        """Adds an item to the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets the item from the cache
        """
        if key and key in self.cache_data:
            return self.cache_data[key]

        return None
