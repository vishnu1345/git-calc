import unittest

from calculator import calculate


class TestCalculator(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(calculate(2, "+", 3), 5)
        self.assertEqual(calculate(7, "-", 2), 5)
        self.assertEqual(calculate(4, "*", 2.5), 10)
        self.assertEqual(calculate(9, "/", 3), 3)

    def test_power_and_modulo(self):
        self.assertEqual(calculate(2, "^", 10), 1024)
        self.assertEqual(calculate(10, "%", 3), 1)
        with self.assertRaises(ValueError):
            calculate(5, "%", 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(1, "/", 0)


if __name__ == "__main__":
    unittest.main()
