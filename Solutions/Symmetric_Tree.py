# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = self.recursive_sol(root, root)
        return res

    def recursive_sol(self, left, right):
        if left is None and right is None:
            return True

        if None in [left, right]:
            return False

        if left.val != right.val:
            return False

        if not self.recursive_sol(left.left, right.right):
            return False

        if not self.recursive_sol(left.right, right.left):
            return False

        return True
