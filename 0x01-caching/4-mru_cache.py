#!/usr/bin/env python3
"""Module that defines MRUCache class
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """Creates a cache with least recently used mechanism
    """
    keys_queue = []

    def put(self, key, item):
        """Inserts an item to the cache
        and discards the most recent used item
        """
        if key and item:
            limit = self.MAX_ITEMS
            cache = self.cache_data
            cache_len = len(cache)

            if cache_len == limit and key not in cache:
                self.discard(self.keys_queue[-1])

            self.used(key)
            self.cache_data[key] = item

    def get(self, key):
        """gets an item from the cache based on the key
        """
        if key and key in self.cache_data:
            self.used(key)
            return self.cache_data[key]

        return None

    def used(self, key):
        """moves the key to the last of the queue
        """
        keys_queue = self.keys_queue
        if key in keys_queue:
            keys_queue.remove(key)

        keys_queue.append(key)

    def discard(self, key):
        """discards the key from the cache
        """
        print(self.keys_queue)
        self.cache_data.pop(key)
        self.keys_queue.pop(-1)
        print("DISCARD:", key)
