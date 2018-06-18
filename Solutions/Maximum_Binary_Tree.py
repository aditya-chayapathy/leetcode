# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.recurssiveSolution(nums)

    def recurssiveSolution(self, A):
        result = TreeNode(max(A))
        if len(A[:A.index(max(A))]) != 0:
            result.left = self.recurssiveSolution(A[:A.index(max(A))])
        if len(A[A.index(max(A)) + 1:]) != 0:
            result.right = self.recurssiveSolution(A[A.index(max(A)) + 1:])

        return result