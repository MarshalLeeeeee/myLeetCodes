'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

Note:
Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head or not head.next):
            return head
        curr = head
        currNext = curr.next
        curr.next = currNext.next
        currNext.next = curr
        res = currNext
        while(curr):
            if(not curr.next or not curr.next.next):
                break
            else:
                currCopy, curr = curr,curr.next
                currNext = curr.next
                curr.next = currNext.next
                currNext.next = curr
                currCopy.next = currNext
        return res
        
class Solution2:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head or not head.next):
            return head
        curr = head
        currNext = curr.next
        curr.next = currNext.next
        currNext.next = curr
        res = currNext
        curr.next = self.swapPairs(curr.next)
        return res