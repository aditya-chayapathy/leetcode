# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.traversal = []

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.recurrsiveSolution(root, 0)

        for i in range(1, len(self.traversal), 2):
            self.traversal[i].reverse()

        return self.traversal

    def recurrsiveSolution(self, root, level):
        if root is None:
            return

        if len(self.traversal) <= level:
            self.traversal.append([])

        self.traversal[level].append(root.val)
        self.recurrsiveSolution(root.left, level + 1)
        self.recurrsiveSolution(root.right, level + 1)
