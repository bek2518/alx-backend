#!/usr/bin/env python3
'''
Creates a LRUCache class which is a caching system
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''
    Class that inherits from BaseCaching and is a caching system that
    implements LRU algorithm
    '''
    tracker = []

    def __init__(self):
        '''
        Initializes BasicCache
        '''
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''
        Places key, item pair to the dictionary using the LRU algorithm
        '''
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
           key not in self.cache_data.keys()):
            first_key = self.tracker[0]
            self.cache_data.pop(first_key)
            print('DISCARD: {}'.format(first_key))
            self.tracker.remove(first_key)

        self.cache_data[key] = item
        if key in self.tracker:
            self.tracker.remove(key)
        self.tracker.append(key)

    def get(self, key):
        '''
        gets the item stored in the dictionry using the key
        '''
        if key is None:
            return None

        if key in self.cache_data.keys():
            self.tracker.remove(key)
            self.tracker.append(key)
            return self.cache_data[key]

        return None
