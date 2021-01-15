#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    # test function max_integer to get biggest int
    def test_max_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_max_negatives(self):
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_max_mixed(self):
        self.assertEqual(max_integer([-4, 3, -2, 1]), 3)

    def test_max_one_int(self):
        self.assertEqual(max_integer([9]), 9)

    @unittest.expectedFailure
    def test_empty_list(self):
        self.assertEqual(max_integer())

if __name__ == '__main__':
    unittest.main()
