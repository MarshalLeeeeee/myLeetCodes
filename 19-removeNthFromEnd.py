'''
19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
'''

def init(nums):
    nodes = []
    for x in nums:
        node = ListNode(x)
        if(len(nodes)>0):
            nodes[-1].next = node
        nodes.append(node)
    return nodes[0]

def showRes(nodes):
    while(nodes):
        print(nodes.val)
        nodes = nodes.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        curr = head
        length = 1
        stack = [ListNode(curr.val)]
        while(curr.next):
            curr = curr.next
            length += 1
            stack.append(ListNode(curr.val))
            stack[-2].next = stack[-1]
        
        if length == 1:
            return None
        elif length == n:
            return stack[1]
        elif n == 1:
            stack[-2].next = None
            return stack[0]
        else:
            stack[-n-1].next = stack[-n+1]
            return stack[0]




if __name__ == '__main__':
    nodes = init([1,2])
    showRes(nodes)
    res = Solution().removeNthFromEnd(nodes,1)
    showRes(res)
