# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursiveSolution(root, root.val)

    def recursiveSolution(self, node, value):
        if node == None:
            return True

        if node.val != value:
            return False

        left_subtree = self.recursiveSolution(node.left, value)
        if not left_subtree:
            return False

        right_subtree = self.recursiveSolution(node.right, value)
        if not right_subtree:
            return False

        return True