'''
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return head
        if m == n: return head
        newHead = ListNode(0)
        newHead.next = head
        currPrev, curr, cnt, flag = newHead, head, 1, False
        while curr:
            if flag:
                currPrev.next = curr.next
                curr.next = start.next
                start.next = curr
                curr = currPrev.next
                if cnt == n: break
            else:
                if cnt == m:
                    start = currPrev
                    flag = True
                currPrev,curr = curr,curr.next
            cnt += 1
        return newHead.next