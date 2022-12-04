"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
from typing import List, Dict
import unittest

staircase_ways: Dict[int, int] = {}

def get_ways(stairs: int, possible_steps: List[int] = [1,2], reset: bool = False) -> int:
    if reset:
        staircase_ways.clear()
    if stairs == 0:
        return 1
    if stairs < 0:
        return 0
    if not possible_steps:
        return 0
    if stairs in staircase_ways:
        return staircase_ways[stairs]
    ways = 0
    for steps_at_onec in possible_steps:
        ways += get_ways(stairs - steps_at_onec, possible_steps)
    staircase_ways[stairs] = ways
    return ways

class Test_P9(unittest.TestCase):
    def test_cases(self):
        assert get_ways(4, reset=True) == 5
        assert get_ways(1, reset=True) == 1
        assert get_ways(2, reset=True) == 2
        assert get_ways(4, [1], reset=True) == 1
        assert get_ways(4, [2], reset=True) == 1
        assert get_ways(4, [1, 3, 5], reset=True) == 3
        assert get_ways(4, [1, 3, 4], reset=True) == 4
        assert get_ways(2, [3], reset=True) == 0
        assert get_ways(4, [3], reset=True) == 0
