"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
from string import ascii_lowercase
from typing import List, Dict
import random
import unittest

def estimate_pi(samples: int) -> float:
    in_circle = 0
    for i in range(samples):
        x = random.random()
        y = random.random()
        if pow(x, 2) + pow(y, 2) <= 1:
            in_circle += 1
    area = 1*1 * in_circle / samples * 4 # a quarter of a circle
    return area # area/r^2 = pi


print(estimate_pi(10000000))
