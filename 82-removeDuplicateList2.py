'''
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
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
        left = ListNode(0)
        left.next = head
        newHead = left
        currNum, currCnt, right = head.val, 1, head.next
        while right:
            if right.val != currNum:
                if currCnt > 1:
                    left.next = right
                else:
                    left = left.next
                currCnt, currNum = 1, right.val
            else: currCnt += 1
            right = right.next
        if currCnt > 1:
            left.next = right
        return newHead.next