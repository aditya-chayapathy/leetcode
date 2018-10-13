# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = self.recurssiveSolution(preorder, inorder)

        return root

    def recurssiveSolution(self, preorder, inorder):
        if len(preorder) == 0 and len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])

        root_index = inorder.index(preorder[0])
        left_inorder_arr = inorder[:root_index]
        right_inorder_arr = inorder[root_index + 1:]

        left_preorder_arr = preorder[1:len(left_inorder_arr) + 1]
        right_preorder_arr = preorder[1 + len(left_inorder_arr):]

        root.left = self.recurssiveSolution(left_preorder_arr, left_inorder_arr)
        root.right = self.recurssiveSolution(right_preorder_arr, right_inorder_arr)

        return root
