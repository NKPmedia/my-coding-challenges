"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4
"""
import unittest
from numbers import Number
from typing import Callable, Union


def cons(a: Union[Number, Callable], b: Union[Number, Callable]) -> Callable:
    def pair(f: Callable) -> Number:
        return f(a, b)

    return pair


def last(a: Union[Number, Callable], b: Union[Number, Callable]) -> Union[Number, Callable]:
    return b


def first(a: Union[Number, Callable], b: Union[Number, Callable]) -> Union[Number, Callable]:
    return a


def car(pair: Callable) -> Union[Number, Callable]:
    return pair(first)


def cdr(pair: Callable) -> Union[Number, Callable]:
    return pair(last)


class Test(unittest.TestCase):

    def test_cases(self):
        assert car(cons(3, 4)) == 3
        assert cdr(cons(3, 4)) == 4
        assert car(cdr(cons(3, cons(4, 5)))) == 4
        assert cdr(cdr(cons(3, cons(4, 5)))) == 5
