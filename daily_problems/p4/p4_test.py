import unittest

from .p4 import first_non_exist


class Test_P4(unittest.TestCase):

    def test_cases(self):
        assert first_non_exist([3, 4, -1, 1]) == 2
        assert first_non_exist([1, 2, 0]) == 3
        assert first_non_exist([1, 2, 1, -9, 0, 2]) == 3
