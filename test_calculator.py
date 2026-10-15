"""Unit tests for calculator arithmetic and error handling."""

import unittest

from calculator import add_numbers, divide


class CalculatorTests(unittest.TestCase):
    """Check ordinary calculations and boundary cases."""

    def test_add_numbers(self) -> None:
        """Check positive, negative, zero, and fractional operands."""
        for a, b, expected in [(2, 3, 5), (-2, -3, -5), (0, 0, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add_numbers(a, b), expected)
        self.assertAlmostEqual(add_numbers(0.1, 0.2), 0.3)

    def test_divide(self) -> None:
        """Check positive, negative, zero, and fractional results."""
        for a, b, expected in [(10, 2, 5), (-9, 3, -3), (0, 5, 0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(divide(a, b), expected)
        self.assertAlmostEqual(divide(1, 4), 0.25)

    def test_divide_by_zero(self) -> None:
        """Check that a zero divisor produces a clear error."""
        for a, b in [(10, 0), (0, 0), (1, -0.0)]:
            with self.subTest(a=a, b=b):
                with self.assertRaisesRegex(
                    ValueError, "Cannot divide by zero"
                ):
                    divide(a, b)


if __name__ == "__main__":
    unittest.main()
