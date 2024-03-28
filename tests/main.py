import unittest
from quotation import divide, total


class TestQuotation(unittest.TestCase):
    def test_divide_returns_correct_value_with_two_decimal_places(self):
        self.assertEqual(divide(1000), '120.00')

    def test_divide_returns_correct_value_with_two_decimal_places_for_fractional_input(self):
        self.assertEqual(divide(1000.5), '120.06')

    def test_total_returns_correct_value_with_two_decimal_places(self):
        self.assertEqual(total(1000), '1120.00')

    def test_total_returns_correct_value_with_two_decimal_places_for_fractional_input(self):
        self.assertEqual(total(1000.5), '1120.56')

    def test_divide_returns_zero_for_zero_input(self):
        self.assertEqual(divide(0), '0.00')

    def test_total_returns_zero_for_zero_input(self):
        self.assertEqual(total(0), '0.00')


if __name__ == '__main__':
    unittest.main()
