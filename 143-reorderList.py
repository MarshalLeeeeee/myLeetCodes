'''
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head and head.next:
            l, curr = 0, head
            while curr:
                l += 1
                curr = curr.next
            mid, curr, currPrev, i = (l+1) // 2, head, None, 0
            print(mid)
            while i < l:
                i += 1
                if i == mid: 
                    currNext = curr.next
                    curr.next = None
                    currPrev, curr = curr, currNext
                elif i == mid + 1:
                    currNext = curr.next
                    curr.next = None
                    currPrev, curr = curr, currNext
                elif i > mid + 1:
                    currNext = curr.next
                    curr.next = currPrev
                    currPrev, curr = curr, currNext
                else: curr = curr.next
            tail = currPrev
            chead, ctail = head.next, tail
            curr = head
            for i in range(1,l):
                if i % 2 == 1:
                    ctailNext = ctail.next
                    ctail.next = None
                    curr.next = ctail
                    ctail = ctailNext
                    curr = curr.next
                else:
                    cheadNext = chead.next
                    chead.next = None
                    curr.next = chead
                    chead = cheadNext
                    curr = curr.next