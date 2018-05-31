# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        
        nodes = []
        while head is not None:
            nodes.append(head.val)
            head = head.next
        
        a = nodes[:-n]
        b = nodes[len(nodes)-n+1:]
        nodes = a + b
        
        temp = ListNode(nodes[0])
        result = temp
        for i in range(1, len(nodes)):
            temp.next = ListNode(nodes[i])
            temp = temp.next
            
        return result
