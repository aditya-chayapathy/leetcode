# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        root = self.recursive_sol(nums, 0, len(nums) - 1)

        return root

    def recursive_sol(self, nums, low, high):
        if low > high:
            return None

        mid = int((low + high) / 2)
        node = TreeNode(nums[mid])
        node.left = self.recursive_sol(nums, low, mid - 1)
        node.right = self.recursive_sol(nums, mid + 1, high)

        return node
