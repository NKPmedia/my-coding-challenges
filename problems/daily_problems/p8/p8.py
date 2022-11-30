"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""
from typing import Tuple
import unittest

class Node():
    def __init__(self,a , left=None, right=None) -> None:
        self.val = a
        self.left = left
        self.right = right

def count_unival_subtree(tree: Node) -> Tuple[int, int]:
    if not tree.left: #Assume that eiter two sibblings or none
        return (1, tree.val)
    else:
        left_unival_subtrees, left_val = count_unival_subtree(tree.left)
        right_unival_subtrees, right_val = count_unival_subtree(tree.right)

        if right_val == tree.val and left_val == tree.val:
            return (left_unival_subtrees + right_unival_subtrees + 1, tree.val)
        else:
            return (left_unival_subtrees + right_unival_subtrees, None)


class Test_P7(unittest.TestCase):

    def test_cases(self):
        tree = Node(0, Node(1),Node(0,Node(1,Node(1),Node(1)),Node(0)))
        assert count_unival_subtree(tree)[0] == 5
