import re

class Node(object):
    def __init__(self, value, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return (self.value, self.left, self.right) == (other.value, other.left, other.right)
            

class RecursiveParser(object):
    @classmethod
    def parse_factor(cls, tokens):
        """Parse a number or a parenthesized expression."""
        
        # remove the first token from the list
        token = tokens.pop(0)

        # if it's a number, return a node with that value
        if type(token) in (float, int):
            return Node(float(token))

        # if it's a left parenthesis
        if token == '(':
            # parse an expression
            node = cls.parse_expression(tokens)

            # remove the right parenthesis
            tokens.pop(0)

            # return the expression
            return node
        
        # if it's a right parenthesis, it's a syntax error
        if token == ')':
            raise SyntaxError('Unexpected right parenthesis')
        

    @classmethod
    def parse_term(cls, tokens):
        """Parse a term, a sequence of factors separated by multiplication or division operators."""
        
        # parse a factor
        node = cls.parse_factor(tokens)

        # while there are more tokens and the next token is a multiplication or division operator
        while tokens and tokens[0] in ('*', '/'):
            # remove the operator from the list
            operator = tokens.pop(0)

            # parse another factor
            right = cls.parse_factor(tokens)

            # create a new node with the operator and two children
            node = Node(operator, left=node, right=right)

        # return the node
        return node
    
    @classmethod
    def parse_expression(cls, tokens):
        """Parse an expression, a sequence of terms separated by addition or subtraction operators."""
        
        # parse a term
        node = cls.parse_term(tokens)

        # while there are more tokens and the next token is an addition or subtraction operator
        while tokens and tokens[0] in ('+', '-'):
            # remove the operator from the list
            operator = tokens.pop(0)

            # parse another term
            right = cls.parse_term(tokens)

            # create a new node with the operator and two children
            node = Node(operator, left=node, right=right)

        # return the node
        return node

def main():
    node = RecursiveParser.parse_expression([3.14, '*', -2.71])
    print(node.value, node.left.value, node.right.value)

main()