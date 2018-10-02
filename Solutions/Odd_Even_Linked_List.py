# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        odd, even = ListNode(head.val), ListNode(head.next.val)
        temp_odd, temp_even = odd, even

        head = head.next.next

        is_odd = True
        while head is not None:
            if is_odd:
                temp_odd.next = ListNode(head.val)
                temp_odd = temp_odd.next
                is_odd = False
            else:
                temp_even.next = ListNode(head.val)
                temp_even = temp_even.next
                is_odd = True
            head = head.next

        temp_odd.next = even

        return odd
