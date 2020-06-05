"""
Program: test_average_scores.py
Author: Rachel Li
Last date modified: 06/03/2020

The purpose of this program is to test average_scores.py.
"""
import unittest
import unittest.mock as mock
from format_output import average_scores as avg

class AverageTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch ('builtins.input', side_effect=[85,90,95]):
            assert avg.average() == 90


if __name__ == '__main__':
    unittest.main()
