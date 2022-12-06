"""
Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability.
"""
from typing import List
import random

def get_uniform_from_stream(stream: List[int]) -> float:
    i = 1
    last_element = None
    for elem in stream:
        if random.random() <= 1/i:
            last_element = elem
        i += 1
    return last_element