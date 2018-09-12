# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        prev_node = None
        curr_node = head
        next_node = curr_node.next

        while next_node != None:
            curr_node.next = prev_node

            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next

        curr_node.next = prev_node

        return curr_node
