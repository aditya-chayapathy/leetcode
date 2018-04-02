# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur_carry = 0
        res = ListNode(None)
        temp = res
        count = 0
        while (l1 != None and l2 != None):
            prev_carry = cur_carry
            cur_carry = 0

            cur_sum = l1.val + l2.val + prev_carry
            if (cur_sum >= 10):
                cur_carry = 1
                cur_sum -= 10

            temp.val = cur_sum
            temp.next = ListNode(None)
            temp = temp.next

            count += 1
            l1 = l1.next
            l2 = l2.next

        while (l1 != None):
            prev_carry = cur_carry
            cur_carry = 0

            cur_sum = l1.val + prev_carry
            if (cur_sum >= 10):
                cur_carry = 1
                cur_sum -= 10

            temp.val = cur_sum
            temp.next = ListNode(None)
            temp = temp.next

            count += 1
            l1 = l1.next

        while (l2 != None):
            prev_carry = cur_carry
            cur_carry = 0

            cur_sum = l2.val + prev_carry
            if (cur_sum >= 10):
                cur_carry = 1
                cur_sum -= 10

            temp.val = cur_sum
            temp.next = ListNode(None)
            temp = temp.next

            count += 1
            l2 = l2.next

        if (l1 == None and l2 == None and cur_carry == 1):
            temp.val = 1
            temp.next = None

            return res

        temp = res
        while (temp.next.val != None):
            temp = temp.next
        temp.next = None

        return res