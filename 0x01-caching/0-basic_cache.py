#!/usr/bin/env python3
'''Module for BasicCache Class'''
BaseCaching =  __import__('base_caching').BaseCaching

class BasicCache(BaseCaching):
    '''BasicCache inheriting from BaseCaching Class'''
    def put(self, key, item):
        '''Must assign to the dictionary self.cache_data the item va\
lue for the key key.If key or item is None, do nothing'''
        if key and item:
            self.cache_data[key] = item
    def get(self, key):
        '''Must return the value in self.cache_data linked to key.If key\
 is None or if the key doesn't exist in self.cache_data, return None'''
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data[key]
