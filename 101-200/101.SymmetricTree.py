#
# 101. Symmetric Tree
#
# Given a binary tree, check whether it is a mirror of itself(ie, symmetric
# around its center).
#
# For example, this binary tree [1, 2, 2, 3, 4, 4, 3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following [1, 2, 2, null, 3, null, 3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#     3   3
#


class Solution:
    def isSymmetric1(self, root) -> bool:
        def check(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            return check(left.left, right.right) and check(left.right, right.left)
        return check(root, root)

    def isSymmetric(self, root):
        queue = [root, root]

        while queue:
            left = queue.pop(0)
            right = queue.pop(0)

            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False

            queue.extend([left.left, right.right, left.right, right.left])
        return True
