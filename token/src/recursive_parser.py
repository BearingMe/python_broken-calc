from .node import Node
from interfaces import AbstractRecursiveParser

class RecursiveParser(AbstractRecursiveParser):
    def parse_factor(self, tokens):
        """Parse a number or a parenthesized expression."""
        
        # remove the first token from the list
        token = tokens.pop(0)

        # if it's a number, return a node with that value
        if type(token) in (float, int):
            return Node(float(token))

        # if it's a left parenthesis
        if token == '(':
            # parse an expression
            node = self.parse_expression(tokens)

            # remove the right parenthesis
            tokens.pop(0)

            # return the expression
            return node

            # if it's a plus or minus operator
        
        # if it's a right parenthesis, it's a syntax error
        if token == ')':
            raise SyntaxError('Unexpected right parenthesis')
        
    def parse_term(self, tokens):
        """Parse a term, a sequence of factors separated by multiplication or division operators."""
        
        # parse a factor
        node = self.parse_factor(tokens)

        # while there are more tokens and the next token is a multiplication or division operator
        while tokens and tokens[0] in ('*', '/'):
            # remove the operator from the list
            operator = tokens.pop(0)

            # parse another factor
            right = self.parse_factor(tokens)

            # create a new node with the operator and two children
            node = Node(operator, left=node, right=right)

        # return the node
        return node
    
    def parse_expression(self, tokens):
        """Parse an expression, a sequence of terms separated by addition or subtraction operators."""
        
        # parse a term
        node = self.parse_term(tokens)

        # while there are more tokens and the next token is an addition or subtraction operator
        while tokens and tokens[0] in ('+', '-'):
            # remove the operator from the list
            operator = tokens.pop(0)

            # parse another term
            right = self.parse_term(tokens)

            # create a new node with the operator and two children
            node = Node(operator, left=node, right=right)

        # return the node
        return node

    def parse(self, tokens):
        """Parse a string into a syntax tree."""
        
        # parse the tokens into a syntax tree
        tree = self.parse_expression(tokens)

        # return the syntax tree
        return tree