'''
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # bf solution
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        queue, curr = [], head
        while curr:
            try: return queue[queue.index(curr)]
            except:
                queue.append(curr)
                curr = curr.next

class Solution(object):
    # double pointer with different speeds
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast, slow, flag = head, head, False
        while fast:
            fast = fast.next.next if fast.next else None
            slow = slow.next
            if fast == slow: break
        if fast:
            # assume 
            # prefix has 'a' nodes (which is the pos)
            # loop has 'b' nodes
            # the meeting point must be in the loop part
            # a + pb + n = 2(a + qb +n), 0 <= n < b, p,q are integers
            # n = (p-2q)b - a = b-a, thus the a-th node next to meeting point is the answer
            fast = head
            while fast != slow:
                fast, slow = fast.next, slow.next
            return fast

if __name__ == '__main__':
    a = ListNode(1)
    c = b = ListNode(1)
    q = [a]
    print(a == b)
    print(a is b)
    print(b in q)
    print(q.index(a))