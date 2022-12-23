from dataclasses import dataclass
from typing import Self

from interfaces import AbstractNode

@dataclass
class Node(AbstractNode):
    value: Self
    left: Self = None
    right: Self = None

    def evaluate(self):
        """evaluate the expression represented by the syntax tree."""
        if not self.left and not self.right:
            # if the node has no children, it's a leaf node
            # return the value of the node as a float
            return float(self.value)

        # if the node has children, it's an operator node
        # evaluate the left and right children
        left_value = self.left.evaluate()
        right_value = self.right.evaluate()

        # apply the operator to the left and right values
        if self.value == '+':
            return left_value + right_value
        elif self.value == '-':
            return left_value - right_value
        elif self.value == '*':
            return left_value * right_value
        elif self.value == '/':
            return left_value / right_value

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False

        return (self.value, self.left, self.right) == (other.value, other.left, other.right)
    
    def __repr__(self):
        output = f"Node({self.value}"

        if self.left:
            output += f", left={self.left}"

        if self.right:
            output += f", right={self.right}"

        output += ")"

        return output
