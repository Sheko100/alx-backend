#!/usr/bin/env python3
"""Module that defines LFUCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Creates a cache with least recently used mechanism
    """
    usage = {}

    def put(self, key, item):
        """Inserts an item to the cache
        and discards the least frequently used item
        """
        if key and item:
            limit = self.MAX_ITEMS
            cache = self.cache_data
            cache_len = len(cache)

            if cache_len == limit and key not in cache:
                self.discard(self.lfu_key())

            if key not in cache:
                self.usage[key] = 0
            else:
                self.usage[key] += 1

            self.cache_data[key] = item

    def get(self, key):
        """gets an item from the cache based on the key
        """
        if key and key in self.cache_data:
            self.usage[key] += 1
            return self.cache_data[key]

        return None

    def lfu_key(self):
        """gets the least used key from the usage dictionary
        """
        usage = self.usage
        least = list(usage.keys())[0]

        for key, value in usage.items():
            if usage[least] > value:
                least = key

        return least

    def discard(self, key):
        """discards the key from the cache
        """
        self.cache_data.pop(key)
        self.usage.pop(key)
        print("DISCARD:", key)
