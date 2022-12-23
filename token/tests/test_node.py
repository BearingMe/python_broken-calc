import unittest

from src import Node

class TestNode(unittest.TestCase):
    def test_node_creation(self):
        # test creating a node with no children
        node = Node(1)
        self.assertEqual(node.value, 1)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

        # test creating a node with left and right children
        node = Node(2, Node(1), Node(3))
        self.assertEqual(node.value, 2)
        self.assertEqual(node.left, Node(1))
        self.assertEqual(node.right, Node(3))

    def test_node_equality(self):
        # test equality of nodes with same value and no children
        node1 = Node(1)
        node2 = Node(1)
        self.assertEqual(node1, node2)

        # test equality of nodes with same value and different children
        node1 = Node(2, Node(1), Node(3))
        node2 = Node(2, Node(1), Node(3))
        self.assertEqual(node1, node2)

        # test inequality of nodes with different values
        node1 = Node(1)
        node2 = Node(2)
        self.assertNotEqual(node1, node2)

        # test inequality of nodes with same values but different children
        node1 = Node(2, Node(1), Node(3))
        node2 = Node(2, Node(3), Node(1))
        self.assertNotEqual(node1, node2)
