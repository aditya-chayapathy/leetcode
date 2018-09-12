# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next

        for i, j in zip(range(len(array)), range(len(array) - 1, -1, -1)):
            if array[i] != array[j]:
                return False

        return True
