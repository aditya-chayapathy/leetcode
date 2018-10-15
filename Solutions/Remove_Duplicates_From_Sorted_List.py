# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
      	"""
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        if head.next is None:
            return head

        slow = head
        fast = head.next
        while fast != None:
            while fast != None and fast.val == slow.val:
                fast = fast.next
            if fast != None:
                slow.next = fast
                slow = slow.next
                fast = fast.next
            else:
                slow.next = None

        return head
