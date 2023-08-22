#!/usr/bin/env python3
'''Module for FIFOCache Class'''
BaseCaching =  __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    '''FIFOCache inheriting from BaseCaching Class'''
    def put(self, key, item):
        '''If the number of items in self.cache_data is higher that BaseCach\
ing.MAX_ITEMS:you must discard the first item put in cache (FIFO algorithm)\
you must print DISCARD: with the key discarded and following by a new line'''
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            popped_key = list(self.cache_data)[0]
            print(f'DISCARD: {popped_key}')
            del self.cache_data[popped_key]
    def get(self, key):
        '''Must return the value in self.cache_data linked to key.If key\
 is None or if the key doesn't exist in self.cache_data, return None'''
        if key is None or not (key in self.cache_data):
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]