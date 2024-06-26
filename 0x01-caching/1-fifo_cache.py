#!/usr/bin/python3
"""Module that defines class FIFOCache
"""
BaseCache = __import__('base_caching').BaseCaching


class FIFOCache(BaseCache):
    """Implements a first in first out cache behavior"""

    def __init__(self):
        """Initialzes the instance"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache and replaces the first item
        if the cache is overload

        Args:
            key: the key of the item
            item: the value that will be associated with the key
        """
        if key is None or item is None:
            return

        if key not in self.queue and len(self.cache_data) == super().MAX_ITEMS:
            first_key = self.queue[0]
            print('DISCARD: {}'.format(first_key))
            del self.cache_data[first_key]
            self.queue = self.queue[1:]
        else:
            self.queue.append(key)

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
