# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sol = self.recursive_sol(root, [], [])

        return sol

    def recursive_sol(self, node, less_than_arr, greater_than_arr):
        if node is None:
            return True

        if len(less_than_arr) > 0:
            error = False
            for item in less_than_arr:
                if item <= node.val:
                    error = True
            if error:
                return False

        if len(greater_than_arr) > 0:
            error = False
            for item in greater_than_arr:
                if item >= node.val:
                    error = True
            if error:
                return False

        left_subtree = True
        if node.left is not None:
            left_subtree = self.recursive_sol(node.left, less_than_arr + [node.val], greater_than_arr)
        right_subtree = True
        if node.right is not None:
            right_subtree = self.recursive_sol(node.right, less_than_arr, greater_than_arr + [node.val])

        if left_subtree and right_subtree:
            return True
        else:
            return False
