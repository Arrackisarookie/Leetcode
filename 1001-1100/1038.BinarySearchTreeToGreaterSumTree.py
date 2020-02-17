#
# 1038. Binary Search Tree to Greater Sum Tree
#
# Given the root of a binary search tree with distinct values, modify it so
# that every node has a new value equal to the sum of the values of the
# original tree that are greater than or equal to node.val.
#
# As a reminder, a binary search tree is a tree that satifies these
# constraints:
#
# ~ The left subtree of a node contains only nodes with keys less than the
#   node's keys.
# ~ The right subtree of a node contains only nodes with keys greater than the
#   node's key.
# ~ Both the left and right subtrees must also be binary search trees.
#
# Example:
#                   4                         30
#               /      \                    /    \
#              1        6                  36    21
#             /  \     /  \       -->     /  \  /  \
#            0    2   5    7             36 35  26 15
#                 \         \                \      \
#                  3         8               33      8
#
# Input: [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, 8]
# Output: [30, 36, 21, 36, 35, 26, 15, null, null, null, 33, null, null,null,8]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if 
        return bstToGst(root.left)