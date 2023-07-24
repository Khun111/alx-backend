#!/usr/bin/env python3
'''Module for function that returns pagination indices'''


def index_range(page: int, page_size: int) -> tuple:
    '''Function that returns pagination indices'''
    s_index = (page - 1) * page_size
    l_index = (s_index + page_size)
    return (s_index, l_index)
