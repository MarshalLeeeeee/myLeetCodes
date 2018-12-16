'''
83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        left, right, currNum, currCnt = head, head.next, head.val, 1
        while right:
            if right.val != currNum:
                if currCnt > 1:
                    left.next = right
                left = left.next
                currNum, currCnt = right.val, 1
            else: currCnt += 1
            right = right.next
        if currCnt > 1:
            left.next = None
        return head