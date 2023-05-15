#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''
        Method that returns indexed dataset based on the index provided
        even if there is deletion
        '''
        indexed_dataset = self.indexed_dataset()
        assert index < len(indexed_dataset) and index > 0
        data = []

        current_index = index
        next_index = index + page_size

        while current_index < next_index:
            if current_index in indexed_dataset.keys():
                data.append(indexed_dataset[current_index])
            else:
                next_index += 1
            current_index += 1

        dictionary = {}
        dictionary['index'] = index
        dictionary['data'] = data
        dictionary['page_size'] = page_size
        dictionary['next_index'] = next_index

        return (dictionary)
