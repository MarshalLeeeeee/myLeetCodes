'''
86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head: return head
        newHead = ListNode(0)
        newHead.next = head
        left, currPrev, curr, flag = newHead, newHead, head, True
        while curr:
            if curr.val < x:
                if flag:
                    ans = curr
                    flag = False
                if curr == left.next: 
                    left = left.next
                    currPrev, curr = curr, curr.next
                    flag = False
                else:
                    currPrev.next = curr.next
                    curr.next, left.next = left.next, curr
                    curr, left = currPrev.next, left.next
            else:
                currPrev, curr = curr, curr.next
        if not flag: return ans
        else: return head

def createList(nodes):
    head = ListNode(0)
    curr = head
    for n in nodes:
        curr.next = ListNode(n)
        curr = curr.next
    print(showList(head.next))
    return head.next

def showList(nodes):
    curr, res = nodes, []
    while(curr):
        res.append(curr.val)
        curr = curr.next
    return res

if __name__ == '__main__':
    nums = [1,4,3,2,5,2]
    nodes = createList(nums)
    res = Solution2().partition(nodes,3)
    print(showList(res))