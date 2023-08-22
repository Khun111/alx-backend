#!/usr/bin/env python3
'''Module for LIFOCache Class'''
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    '''LFUCache inheriting from BaseCaching Class'''

    def __init__(self):
        super().__init__()
        self.order = []
        self.freq_track = {}
        self.min_freq = 0

    def put(self, key, item):
        '''If items in cache is higher that BaseCaching.MAX_ITEMS:\
you must discard the least frequency used item (LFU algorithm) if you find \
more than 1 item to discard, you must use the LRU algorithm to discard only \
the least recently used you must print DISCARD: with the key discarded \
and following by a new line'''
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.freq_track[key] += 1
            self.min_freq = min(self.min_freq, self.freq_track[key])
            self.cache_data[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                popped_key = min(
                    self.freq_track, key=lambda x: self.freq_track[x])
                print(f'DISCARD: {popped_key}')
                del self.cache_data[popped_key]
                del self.freq_track[popped_key]
            self.freq_track[key] = 1
            self.min_freq = 1
            self.cache_data[key] = item

    def get(self, key):
        '''Must return the value in self.cache_data linked to key.If key\
 is None or if the key doesn't exist in self.cache_data, return None'''
        if key is None or key not in self.cache_data:
            return None
        self.freq_track[key] += 1
        self.min_freq = min(self.min_freq, self.freq_track[key])
        return self.cache_data[key]
