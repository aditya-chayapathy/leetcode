# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def __init__(self):
        self.traversal = []

    def connect(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.recurrsiveSolution(root, 0)

        result = []
        for i in range(len(self.traversal)):
            for j in range(len(self.traversal[i]) - 1):
                self.traversal[i][j].next = self.traversal[i][j + 1]
            self.traversal[i][-1] = None

    def recurrsiveSolution(self, root, level):
        if root is None:
            return

        if len(self.traversal) <= level:
            self.traversal.append([])

        self.traversal[level].append(root)
        self.recurrsiveSolution(root.left, level + 1)
        self.recurrsiveSolution(root.right, level + 1)
