'''
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head:
            newHead = ListNode(0)
            newHead.next = head
            currPrev, curr = newHead, head
            while curr:
                if curr.val == val:
                    currPrev.next = curr.next
                    curr = curr.next
                else: currPrev,curr = curr,curr.next
            return newHead.next
        