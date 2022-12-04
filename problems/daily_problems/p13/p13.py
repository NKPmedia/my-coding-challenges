"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
from string import ascii_lowercase
from typing import List, Dict
import unittest

def get_longest_substring(string: str, max_different: int) -> int:
    max_length = 0
    for start_i in range(len(string)):
        included_chars: List[str] = []
        current_length = 0
        while len(included_chars) <= max_different and start_i + current_length < len(string):
            if current_length > max_length:
                max_length = current_length
            new_char = string[start_i + current_length]
            if new_char not in included_chars:
                included_chars.append(new_char)
            current_length += 1
    return max_length

def get_longest_substring_fast(string: str, max_different: int) -> int:
    assert max_different >= 1
    assert len(string) >= 1
    left_i = 0
    right_i = 0
    max_length = 1
    char_count: Dict[str, int] = {}
    for c in ascii_lowercase:
        char_count[c] = 0
    char_count[string[0]] = 1
    while right_i < len(string) - 1:
        right_i += 1
        new_char = string[right_i]
        if char_count[new_char] > 0:
            char_count[new_char] += 1
            if right_i - left_i + 1 > max_length:
                max_length = right_i - left_i + 1
        else:
            while sum_non_null(char_count) >= max_different:
                char_count[string[left_i]] -= 1
                left_i += 1
            char_count[new_char] += 1
            if right_i - left_i + 1 > max_length:
                max_length = right_i - left_i + 1
    return max_length

def sum_non_null(d: Dict[str, int]) -> int:
    sum = 0
    for _, elem in d.items():
        if elem != 0:
            sum += 1
    return sum
class Test_P13(unittest.TestCase):
    def test_cases(self):
        assert get_longest_substring_fast("abcba", max_different=2) == 3
        assert get_longest_substring_fast("abcba", max_different=1) == 1
        assert get_longest_substring_fast("abba", max_different=1) == 2
