import unittest
from src import calc

class TestCalc(unittest.TestCase):
    def test_simple_addition(self):
        self.assertEqual(calc("1 + 2"), 3)
    
    def test_simple_subtraction(self):
        self.assertEqual(calc("5 - 3"), 2)
    
    def test_simple_multiplication(self):
        self.assertEqual(calc("2 * 3"), 6)
    
    def test_simple_division(self):
        self.assertEqual(calc("6 / 2"), 3)
    
    def test_more_complex_expression(self):
        self.assertEqual(calc("1 + 2 * (3 - 4) / 5"), 0.6)
    
    def test_multiple_operations(self):
        self.assertEqual(calc("2 + 3 * 4 - 6 / 3"), 12)
    
    def test_parentheses(self):
        self.assertEqual(calc("(2 + 3) * 4"), 20)
    
    def test_decimal_numbers(self):
        self.assertEqual(calc("2.5 + 3.5"), 6)
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc("2 / 0")
    
    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            calc("invalid expression")
    
    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            calc("")
    
    def test_trailing_operator(self):
        with self.assertRaises(ValueError):
            calc("2 +")
    
    def test_multiple_leading_operators(self):
        with self.assertRaises(ValueError):
            calc("++2")
    
    def test_multiple_trailing_operators(self):
        with self.assertRaises(ValueError):
            calc("2++")
    
    def test_multiple_operators_in_a_row(self):
        with self.assertRaises(ValueError):
            calc("2+++2")
    
    def test_two_minuses_in_a_row(self):
        with self.assertRaises(ValueError):
            calc("2----2")
    
    def test_invalid_characters(self):
        with self.assertRaises(ValueError):
            calc("2 + 2$")

    def test_leading_operator(self):
        self.assertEqual(calc("+ 2"), 2)
        
    def test_exponents_with_decimals(self):
        with self.assertRaises(ValueError):
            calc("2.5 ** 2")

    def test_negative_numbers(self):
        self.assertEqual(calc("-2 + 3"), 1)

    def test_exponentiation(self):
        with self.assertRaises(ValueError):
            calc("2 ^ 3")
