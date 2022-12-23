import unittest

from src import Node, RecursiveParser

class TestRecursiveParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = RecursiveParser()

    def test_parse_factor(self):
        # test parsing a float, int, and parenthesized expression
        self.assertEqual(self.parser.parse_factor([3.14]), Node(3.14))
        self.assertEqual(self.parser.parse_factor([1]), Node(1.0))
        self.assertEqual(self.parser.parse_factor(['(', 3.14, ')']), Node(3.14))

        # test that an error is raised if the input is invalid
        with self.assertRaises(IndexError):
            self.parser.parse_factor(['('])
    
    def test_parse_term(self):
        # test parsing a single factor
        self.assertEqual(self.parser.parse_term([3.14]), Node(3.14))

        # test parsing a factor followed by a multiplication or division operator
        self.assertEqual(self.parser.parse_term([3.14, '*', 2.71]), Node('*', Node(3.14), Node(2.71)))
        self.assertEqual(self.parser.parse_term([3.14, '/', 2.71]), Node('/', Node(3.14), Node(2.71)))

        # test parsing a factor with both multiplication and division operators
        self.assertEqual(self.parser.parse_term([3.14, '*', 2.71, '/', 1.41]), Node('/', Node('*', Node(3.14), Node(2.71)), Node(1.41)))
    
    def test_parse_expression(self):
        # test parsing a single term
        self.assertEqual(self.parser.parse_expression([3.14]), Node(3.14))

        # test parsing a term followed by an addition or subtraction operator
        self.assertEqual(self.parser.parse_expression([3.14, '+', 2.71]), Node('+', Node(3.14), Node(2.71)))
        self.assertEqual(self.parser.parse_expression([3.14, '-', 2.71]), Node('-', Node(3.14), Node(2.71)))

        # test parsing a term with both addition and subtraction operators
        self.assertEqual(self.parser.parse_expression([3.14, '+', 2.71, '-', 1.41]), Node('-', Node('+', Node(3.14), Node(2.71)), Node(1.41)))
