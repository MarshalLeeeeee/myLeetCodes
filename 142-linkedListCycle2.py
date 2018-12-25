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

if __name__ == '__main__':
    a = ListNode(1)
    c = b = ListNode(1)
    q = [a]
    print(a == b)
    print(a is b)
    print(b in q)
    print(q.index(a))