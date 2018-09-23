# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.recursive_sol(root, 0)

        return self.res

    def recursive_sol(self, node, level):
        if node is None:
            return

        if len(self.res) < level + 1:
            self.res.append([])

        self.res[level].append(node.val)
        self.recursive_sol(node.left, level + 1)
        self.recursive_sol(node.right, level + 1)
