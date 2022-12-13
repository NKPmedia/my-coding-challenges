"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping),
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""
from string import ascii_lowercase
from typing import List, Dict, Tuple
import unittest

def get_min_rooms(times: List[Tuple[int, int]]) -> int:
    times_start = [(tmp[0],True) for tmp in times] #O(n)
    times_end = [(tmp[1],False) for tmp in times] #O(n)
    times_together = times_start + times_end
    times_sorted = sorted(times_together, key=lambda x:x[0]) #O(nlog(n))
    rooms_max = 0
    rooms_current = 0
    for time, start in times_sorted: #O(n)
        if start:
            rooms_current += 1
            if rooms_current > rooms_max:
                rooms_max = rooms_current
        else:
            rooms_current -=1
    return rooms_max

class Test_P21(unittest.TestCase):
    def test_cases(self):
        assert get_min_rooms([(30, 75), (0, 50), (60, 150)]) == 2
        assert get_min_rooms([(0, 5), (1, 2), (1, 10)]) == 3
        assert get_min_rooms([(0, 5), (1, 2), (6, 10)]) == 2
