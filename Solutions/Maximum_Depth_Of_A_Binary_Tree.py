# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.recursive_tree_depth(root, 1)

        return max(self.res)

    def recursive_tree_depth(self, node, count):
        if node.left is None and node.right is None:
            self.res.append(count)
            return

        if node.left is not None:
            self.recursive_tree_depth(node.left, count + 1)

        if node.right is not None:
            self.recursive_tree_depth(node.right, count + 1)
