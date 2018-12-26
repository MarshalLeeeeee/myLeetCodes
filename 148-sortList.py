'''
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def solve(self,head,length):
        if length == 1: return head
        i, curr = 0, head
        while i+1 < length//2:
            curr = curr.next
            i += 1
        tail = curr.next
        curr.next = None
        newHead = self.solve(head,length//2)
        newTail = self.solve(tail,length-length//2)
        currHead, currTail, ansHead = newHead, newTail, ListNode(0)
        curr = ansHead
        while currHead and currTail:
            if currHead.val < currTail.val: curr.next = currHead; currHead = currHead.next
            else: curr.next = currTail; currTail = currTail.next
            curr = curr.next
        if not currHead: curr.next = currTail
        else: curr.next = currHead
        return ansHead.next
        
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l, curr = 0, head
        while curr:
            l += 1
            curr = curr.next
        if not l or l == 1: return head
        else: return self.solve(head,l)