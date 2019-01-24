# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is None and t2 is None:
            return None

        root = TreeNode(None)
        self.recursiveSolution(root, t1, t2)

        return root

    def recursiveSolution(self, node, t1, t2):
        node.val = 0
        if t1 is not None:
            node.val += t1.val
        if t2 is not None:
            node.val += t2.val

        if (t1 is not None and t1.left is not None) or (t2 is not None and t2.left is not None):
            node.left = TreeNode(None)
            arg1 = None
            if t1 is None:
                arg1 = None
            else:
                arg1 = t1.left
            arg2 = None
            if t2 is None:
                arg2 = None
            else:
                arg2 = t2.left
            self.recursiveSolution(node.left, arg1, arg2)

        if (t1 is not None and t1.right is not None) or (t2 is not None and t2.right is not None):
            node.right = TreeNode(None)
            arg1 = None
            if t1 is None:
                arg1 = None
            else:
                arg1 = t1.right
            arg2 = None
            if t2 is None:
                arg2 = None
            else:
                arg2 = t2.right
            self.recursiveSolution(node.right, arg1, arg2)
