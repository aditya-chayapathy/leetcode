# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.traversal = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.recurrsiveSolution(root)

        return self.traversal

    def recurrsiveSolution(self, root):
        if root is None:
            return

        self.recurrsiveSolution(root.left)
        self.traversal.append(root.val)
        self.recurrsiveSolution(root.right)
