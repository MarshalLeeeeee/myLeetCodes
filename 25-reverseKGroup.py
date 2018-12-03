'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
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
    print()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if (k <= 1):
            return head
        if (not head or not head.next):
            return head
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        if(k > length):
            return head
        #print('aaaaaaaa')
        curr = head
        currPrev = None
        currNext = curr.next
        n = k - 1
        while(n):
            currPrev,curr,currNext = curr,currNext,currNext.next
            curr.next = currPrev
            n -= 1
        head.next = self.reverseKGroup(currNext,k)
        return curr

class Solution2:
    # very strong and effecient
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        cur.next, l, r = head, head, head
        while True:
            for _ in range(k):
                if r: r=r.next
                else: return dummy.next
            for _ in range(k):
                l.next, r, l = r, l, l.next
            cur.next, r, cur = r, l, cur.next

if __name__ == '__main__':
    nodes = init([1,2,3,4,5])
    res = Solution().reverseKGroup(nodes,3)
    showRes(res)