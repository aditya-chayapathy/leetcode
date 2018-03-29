# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None and l2 == None):
            return []

        if (l1 == None and l2 != None):
            return l2

        if (l1 != None and l2 == None):
            return l1

        i = l1
        j = l2
        k = None
        count = 0
        while (i != None and j != None):
            count += 1
            val = None
            if (i.val <= j.val):
                val = i.val
                i = i.next
            else:
                val = j.val
                j = j.next
            if count == 1:
                res = ListNode(val)
                k = res
            else:
                k.next = ListNode(val)
                k = k.next

        while (i != None):
            k.next = ListNode(i.val)
            k = k.next
            i = i.next

        while (j != None):
            k.next = ListNode(j.val)
            k = k.next
            j = j.next

        return res