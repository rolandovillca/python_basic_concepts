import unittest
from calculator import Calculator

class CalculatorUnitTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_sum(self):
        self.assertEqual(self.calculator.sum(2, 5), 7)

    def test_sub(self):
        self.assertEqual(self.calculator.sub(10, 10), 0)

    def test_mul(self):
        self.assertEqual(self.calculator.mul(10, 10), 100)

    def test_div(self):
        self.assertEqual(self.calculator.div(20, 10), 2)

if __name__ == "__main__":
    unittest.main()

# ============================================
# To run this test, execute following command:
# python2.7 test_calculator_with_unittest.py
# ============================================
