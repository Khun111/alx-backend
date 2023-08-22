#!/usr/bin/python3
"""2-lifo_cache module"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        # Maintain the order of keys by insertion time (most recent first)
        self.order = []

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        return -1

    def put(self, key, value):
        if key in self.cache_data:
            # Update value (no change in order)
            self.cache_data[key] = value
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the least recently added key (last item in order)
                lru_key = self.order.pop()
                print(f'DISCARD: {lru_key}')
                del self.cache_data[lru_key]
            self.cache_data[key] = value
        # Add the key to the front (most recent)
        self.order.append(key)


if __name__ == "__main__":
    my_cache = LIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
    my_cache.put("G", "San Francisco")
    my_cache.print_cache()
