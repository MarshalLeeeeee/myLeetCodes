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
        if(not l1 and not l2):
            return None
        elif(l1 and not l2):
            return l1
        elif(not l1 and l2):
            return l2
        else:
            v1, v2 = l1.val, l2.val
            if (v1 < v2):
                head = ListNode(v1)
                l1 = l1.next
            else:
                head = ListNode(v2)
                l2 = l2.next
            curr = head
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            if (v1 < v2):
                node = ListNode(v1)
                curr.next = node
                curr = curr.next
                l1 = l1.next
            else:
                node = ListNode(v2)
                curr.next = node
                curr = curr.next
                l2 = l2.next
            
        if(l1):
            curr.next = l1
            return head
        elif(l2):
            curr.next = l2
            return head
        else:
            return head
        