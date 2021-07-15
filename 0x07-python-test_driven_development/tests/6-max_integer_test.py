#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer
    """

    def test_max_normal(self):
        """Test normal int
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 4]), 4)

    def test_max_empty(self):
        """Test empty list
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_max_neg(self):
        """Test negative int
        """
        self.assertEqual(max_integer([-1, -2, -10, -4]), -1)

    def test_max_unique(self):
        """Test unique int
        """
        self.assertEqual(max_integer([4]), 4)

    def test_max_error(self):
        """Test errors
        """
        self.assertRaises(TypeError, max_integer, [2, "c"])

    def test_max_middle(self):
        """Test max in the middle
        """
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

if __name__ == '__main__':
    unittest.main()