"""
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox',
and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
import copy
from typing import List, Union, Dict
import unittest

def reconstruct(sentence: str, words: List[str]) -> Union[List[str],None]:
    if sentence == "":
        return []
    words_current = copy.deepcopy(words)
    for i in range(len(sentence)):
        if len(words_current) == 0:
            return None
        char = sentence[i]
        for word in words_current:
            if word[i] != char:
                words_current.remove(word)
            else:
                if len(word) == i+1:
                    words_current.remove(word)
                    construction = reconstruct(sentence[i+1:], words)
                    if construction is not None:
                        return [word] + construction
    return None

def reconstruct_dict_start(sentence: str, words: List[str]) -> List[str]:
    word_dict = {}
    max_word_length = max([len(word) for word in words])
    for word in words:
        word_dict[word] = True

    res = reconstruct_dict(sentence, word_dict, 0, {}, max_word_length)
    if res:
        return res
    return []
def reconstruct_dict(sentence: str, word_dict: Dict[str, bool], global_position: int, cache: Dict[int, Union[List[str], None]], max_word_length: int) -> Union[List[str], None]:
    if sentence == "":
        return []
    if global_position in cache:
        return cache[global_position]
    for i in range(len(sentence)):
        if i+1 > max_word_length:
            cache[global_position] = None
            return None
        subword = sentence[:i+1]
        if subword in word_dict:
            construction = reconstruct_dict(sentence[i + 1:], word_dict, global_position + i + 1, cache, max_word_length)
            if construction is not None:
                cache[global_position] = [subword] + construction
                return [subword] + construction
    cache[global_position] = None
    return None

class Test_P22(unittest.TestCase):
    def test_cases(self):
        assert reconstruct("thequickbrownfox", ['quick', 'brown', 'the', 'fox']) == ['the', 'quick', 'brown', 'fox']
        assert reconstruct("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']) in [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]
        assert reconstruct("bedbathgoandbeyond", ['bed', 'bath', 'bedbathgo', 'and', 'beyond']) in [['bedbathgo', 'and', 'beyond']]

        assert reconstruct_dict_start("thequickbrownfox", ['quick', 'brown', 'the', 'fox']) == ['the', 'quick', 'brown', 'fox']
        assert reconstruct_dict_start("bedbathandbeyond", ['bed', 'bath', 'bedbath', 'and', 'beyond']) in [
            ['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]
        assert reconstruct_dict_start("bedbathgoandbeyond", ['bed', 'bath', 'bedbathgo', 'and', 'beyond']) in [
            ['bedbathgo', 'and', 'beyond']]

        assert reconstruct_dict_start("abcde", ["a", "b", "ab", "de", "d", "abc"]) in [
            ["abc", "de"]]
