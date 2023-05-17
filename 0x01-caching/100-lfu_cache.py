#!/usr/bin/env python3
'''
Creates a LFUCache class which is a caching system
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''
    Class that inherits from BaseCaching and is a caching system that
    implements LFU algorithm
    '''
    tracker = {}

    def __init__(self):
        '''
        Initializes BasicCache
        '''
        BaseCaching.__init__(self)

    def put(self, key, item):
        '''
        Places key, item pair to the dictionary using the LFU algorithm
        Checks for the least used value and if multiple values, removes
        the one least recently used
        '''
        if key is None or item is None:
            return

        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
           key not in self.cache_data.keys()):
            temp = min(self.tracker.values())
            least_keys = []
            for tracker_key in self.tracker.keys():
                if self.tracker[tracker_key] == temp:
                    least_keys.append(tracker_key)

            if len(least_keys) == 1:
                self.cache_data.pop(least_keys[0])
                self.tracker.pop(least_keys[0])
                print('DISCARD: {}'.format(least_keys[0]))
            elif len(least_keys) > 1:
                key_list = []
                for track_key in self.tracker.keys():
                    key_list.append(track_key)
                for i in range(len(key_list)):
                    if key_list[i] in least_keys:
                        self.cache_data.pop(key_list[i])
                        self.tracker.pop(key_list[i])
                        print('DISCARD: {}'.format(key_list[i]))
                        break

        if key in self.tracker:
            count = self.tracker[key]
            self.tracker.pop(key)
        else:
            count = 0
        self.tracker[key] = count + 1
        self.cache_data[key] = item

    def get(self, key):
        '''
        gets the item stored in the dictionry using the key
        '''
        if key is None:
            return None

        if key in self.cache_data.keys():
            count = self.tracker[key]
            self.tracker.pop(key)
            self.tracker[key] = count + 1
            return self.cache_data[key]

        return None
