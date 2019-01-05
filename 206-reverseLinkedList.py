'''
206. Reverse Linked List

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # recursion solution
    def solve(self,node):
        if node.next:
            head,tail = self.solve(node.next)
            node.next = None
            tail.next = node
            return head,node
        else: return node, node
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            h,t = self.solve(head)
            return h
        
class Solution2:
    # iteration solution
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            currPrev, curr = None, head
            while curr:
                currNext = curr.next
                curr.next = currPrev
                currPrev, curr = curr, currNext
            return currPrev