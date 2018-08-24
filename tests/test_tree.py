import unittest


from tree.generate_tree import Tree
from tree.generate_tree import Node


class TestTree(unittest.TestCase):
    def test_OneNode(self):
        root = Node(1, None, None)
        OneNode = Tree(root)
        assert OneNode.visualize_tree() == [[1]]

    def test_Symmetric(self):
        root = Node(1, None, None)
        root.left = Node(2, None, None)
        root.right = Node(3, None, None)
        root.left.left = Node(4, None, None)
        root.left.right = Node(5, None, None)
        root.right.left = Node(6, None, None)
        root.right.right = Node(7, None, None)
        SymTree = Tree(root)
        assert SymTree.visualize_tree() == [['|', '|', '|', 1, '|', '|', '|'],
                                            ['|', 2, '|', '|', '|', 3, '|'],
                                            [4, '|', 5, '|', 6, '|', 7]]

    def test_OneSide(self):
        root = Node(1, None, None)
        root.left = Node(2, None, None)
        root.left.left = Node(4, None, None)
        root.left.left.left = Node(8, None, None)
        OneSideTree = Tree(root)
        assert OneSideTree.visualize_tree() == [['|', '|', '|', '|', '|', '|', '|', 1,
                                                 '|', '|', '|', '|', '|', '|', '|'],
                                                ['|', '|', '|', 2, '|', '|', '|', '|', '|',
                                                 '|', '|', '|', '|', '|', '|'],
                                                ['|', 4, '|', '|', '|', '|', '|', '|', '|',
                                                 '|', '|', '|', '|', '|', '|'],
                                                [8, '|', '|', '|', '|', '|', '|', '|', '|',
                                                 '|', '|', '|', '|', '|', '|']]

    def test_irregular(self):
        root = Node(1, None, None)
        root.left = Node(2, None, None)
        root.right = Node(3, None, None)
        root.left.right = Node(5, None, None)
        root.right.left = Node(6, None, None)
        root.right.left.right = Node(13, None, None)
        irregularTree = Tree(root)
        assert irregularTree.visualize_tree() == [['|', '|', '|', '|', '|', '|', '|', 1,
                                                   '|', '|', '|', '|', '|', '|', '|'],
                                                  ['|', '|', '|', 2, '|', '|', '|', '|', '|',
                                                   '|', '|', 3, '|', '|', '|'],
                                                  ['|', '|', '|', '|', '|', 5, '|', '|',
                                                   '|', 6, '|', '|', '|', '|', '|'],
                                                  ['|', '|', '|', '|', '|', '|', '|', '|',
                                                   '|', '|', 13, '|', '|', '|', '|']]
