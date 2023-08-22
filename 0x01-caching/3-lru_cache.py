#!/usr/bin/env python3
'''Module for LIFOCache Class'''
BaseCaching =  __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    '''FIFOCache inheriting from BaseCaching Class'''
    def __init__(self):
        super().__init__()
        self.order = []
    def put(self, key, item):
        '''If the number of items in self.cache_data is higher that BaseCach\
ing.MAX_ITEMS:you must discard the first item put in cache (FIFO algorithm)\
you must print DISCARD: with the key discarded and following by a new line'''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped_key = self.order.pop(0)
                print(f'DISCARD: {popped_key}')
                del self.cache_data[popped_key]
            self.cache_data[key] = item
            self.order.append(key)
    def get(self, key):
        '''Must return the value in self.cache_data linked to key.If key\
 is None or if the key doesn't exist in self.cache_data, return None'''
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
