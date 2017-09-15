import pytest
from calculator import Calculator

calc = Calculator()

def test_sum():
    assert calc.sum(10, 10) == 20

def test_sub():
    assert calc.sub(10, 10) == 0

def test_mul():
    assert calc.mul(10, 10) == 100

def test_div():
    assert calc.div(10, 10) == 1

# =========================================
# To run these tests run following command:
# py.test test_calculator_with_pytest.py
# =========================================
