"""
You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.

"""
from typing import List
import random

class Log():
    def __init__(self, length: int):
        self.length = length
        self.log = [i for i in range(length)] # store array in memory
        self.next_elem = 0
        self.num_stored = 0

    def record(self, id: int):
        self.log[self.next_elem] = id
        self.next_elem += 1
        self.next_elem = self.next_elem % self.length
        self.num_stored += 1

    def get_last(self, i: int):
        if self.num_stored >= self.length:
            return self.log[(self.next_elem + (i - 1)) % self.length]
        else:
            return self.log[self.next_elem - self.num_stored + (i - 1)]
