"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place
"""
from typing import List


def first_non_exist(numbers: List) -> int:
    i = 0
    next_check = 1
    while(i < len(numbers)):
        if next_check - 1 == i:
            if numbers[next_check - 1] == next_check:
                i += 1
                next_check = i + 1
            elif numbers[next_check - 1] <= 0:
                numbers[next_check - 1] = -1
                i += 1
                next_check = i + 1
            else:
                tmp = numbers[next_check - 1]
                numbers[next_check - 1] = -1
                next_check = tmp
        else:
            if numbers[next_check - 1] == next_check:
                next_check = i + 1
            elif numbers[next_check - 1] <= 0:
                numbers[next_check - 1] = next_check
                next_check = i + 1
            else:
                tmp = numbers[next_check - 1]
                numbers[next_check - 1] = next_check
                next_check = tmp

    for i, j in enumerate(numbers):
        if j != i + 1:
            return i + 1
    return -1
