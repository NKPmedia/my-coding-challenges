import unittest

from .p5 import car, cdr, cons


class Test_P5(unittest.TestCase):

    def test_cases(self):
        assert car(cons(3, 4)) == 3
        assert cdr(cons(3, 4)) == 4
        assert car(cdr(cons(3, cons(4, 5)))) == 4
        assert cdr(cdr(cons(3, cons(4, 5)))) == 5
        