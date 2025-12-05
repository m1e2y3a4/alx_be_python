#!/usr/bin/python3
"""
Unit tests for the SimpleCalculator class.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Tests for the SimpleCalculator basic arithmetic operations."""

    def setUp(self):
        """Create a new SimpleCalculator before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply method."""
        # simple positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # negative * positive
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # anything times zero is zero
        self.assertEqual(self.calc.multiply(7, 0), 0)

    def test_divide(self):
        """Test the divide method, including division by zero."""
        # normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        # divide by zero should return None
        self.assertEqual(self.calc.divide(5, 0), None)


if __name__ == "__main__":
    unittest.main()
