#!/usr/bin/env python3
'''
Creates a FIFOCache class which is a caching system
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''
    Class that inherits from BaseCaching and is a caching system that
    implements FIFO algorithm
    '''
    def __init__(self):
        '''
        Initializes BasicCache
        '''
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''
        Places key, item pair to the dictionary
        '''
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
           key not in self.cache_data.keys()):
            first_key = next(iter(self.cache_data))
            self.cache_data.pop(first_key)
            print('DISCARD: {}'.format(first_key))
            self.cache_data[key] = item

        elif key in self.cache_data.keys():
            self.cache_data[key] = item
        self.cache_data[key] = item

    def get(self, key):
        '''
        gets the item stored in the dictionry using the key
        '''
        if key is None:
            return None

        if key in self.cache_data.keys():
            return self.cache_data[key]

        return None
