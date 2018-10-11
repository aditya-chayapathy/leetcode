# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA = 0
        tempA = headA
        while tempA is not None:
            lenA += 1
            tempA = tempA.next

        lenB = 0
        tempB = headB
        while tempB is not None:
            lenB += 1
            tempB = tempB.next

        if lenA > lenB:
            while lenA != lenB:
                headA = headA.next
                lenA -= 1
        elif lenB > lenA:
            while lenA != lenB:
                headB = headB.next
                lenB -= 1

        while headA is not None and headB is not None and headA != headB:
            headA = headA.next
            headB = headB.next

        return headA
