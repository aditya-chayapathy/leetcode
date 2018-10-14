# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.traversal = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.recurrsiveTraversal(root)

        return self.traversal[k - 1]

    def recurrsiveTraversal(self, root):
        if root is None:
            return

        self.recurrsiveTraversal(root.left)
        self.traversal.append(root.val)
        self.recurrsiveTraversal(root.right)
