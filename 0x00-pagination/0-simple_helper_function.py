#!/usr/bin/env python3
'''
Function that returns a tuple containing start and end index
in corresponding to range of indexes to return in a list for
the particular pagination parameters
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    Function that takes page and page size and returns a tuple with
    start index and end index
    '''
    start_index = (page - 1) * page_size
    end_index = page * page_size

    return (start_index, end_index)
