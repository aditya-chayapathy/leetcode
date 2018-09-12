# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False

        ptr = head
        fast_ptr = head
        while None not in [ptr, fast_ptr]:
            ptr = ptr.next
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                return False
            else:
                fast_ptr = fast_ptr.next

            if ptr == fast_ptr:
                return True

        return False
