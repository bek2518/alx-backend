#!/usr/bin/env python3
'''
Implements Hypermedia pagination
'''
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''
    Function that takes page and page size and returns a tuple with
    start index and end index
    '''
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Function that uses index_range to find the correct indexes
        to paginate the dataset correctly and return the appropriate
        page of the dataset
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        index = index_range(page, page_size)
        dataset = self.dataset()
        indexed = []

        if index[0] > (len(dataset) - 1) or index[1] > (len(dataset) - 1):
            return []

        i = index[0]
        for i in range(index[0], index[1]):
            indexed.append(dataset[i])
            i += 1
        return (indexed)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        Method that takes page and page size and returns dictionary containing
        page_size, page, data, next_page, prev_page, total_pages
        '''
        indexed = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1
        prev_page = page - 1

        if len(indexed) == 0:
            page_size = 0
            next_page = None

        if prev_page == 0:
            prev_page = None

        dictionary = {}
        dictionary['page_size'] = page_size
        dictionary['page'] = page
        dictionary['data'] = indexed
        dictionary['next_page'] = next_page
        dictionary['prev_page'] = prev_page
        dictionary['total_pages'] = total_pages

        return (dictionary)
