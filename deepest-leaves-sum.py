# Problem originally defined at  https://leetcode.com/problems/deepest-leaves-sum/
# Given a binary tree, return the sum of values of its deepest leaves.

from typing import Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int):
        self.val: int = x
        self.left = None
        self.right = None


def deepest_leaves_sum(root: Union[TreeNode, None]) -> int:
    assert root is not None

    sums = {}

    def recurse(node: TreeNode, level: int) -> None:

        if node is None:
            return

        if level in sums:
            sums[level] += node.val
        else:
            sums[level] = node.val

        recurse(node.left, level + 1)
        recurse(node.right, level + 1)

    recurse(root, 0)

    return sums[len(sums) - 1]


# ===================================

# Build a small test case.
node_1 = TreeNode(2)
node_2 = TreeNode(4)
node_3 = TreeNode(6)
node_4 = TreeNode(8)
node_5 = TreeNode(10)
node_6 = TreeNode(12)
node_7 = TreeNode(14)
node_8 = TreeNode(16)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_3.right = node_6
node_4.left = node_7
node_6.right = node_8

sum_of_deepest = deepest_leaves_sum(node_1)  #=> 30
print(sum_of_deepest)
assert sum_of_deepest == 30
