#!/usr/bin/env python3
'''
Creates a BasicCache class which is a caching system
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Class that inherits from BaseCaching and is a caching system
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
