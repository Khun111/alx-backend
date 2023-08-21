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

    def handle_deletion(self, data: List, index: int) -> List:
        '''Method to handle deletion'''
        altered_data = []
        dataset = self.indexed_dataset()
        for row in data:
            if dataset.get(index) is not None:
                altered_data.append(row)
            index += 1
        return altered_data

    def find_available_index(self, index):
        '''Method to find next index'''
        dataset = self.indexed_dataset()
        for i in dataset:
            if dataset.get(index) is None:
                index += 1
        return index

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        dataset = self.indexed_dataset()
        assert index is not None or (index >= 0 and index < len(dataset))
        next_index = index + page_size
        data = [dataset.get(i) for i in range(index, index + page_size)]
        data = self.handle_deletion(data, index)
        available_index = self.find_available_index(index + page_size)
        index = index if len(data) >= page_size else available_index
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index,
        }
