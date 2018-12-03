'''
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        length = len(lists)
        if(length == 0):
            return None
        if(length == 1):
            return lists[0]
        head,tail = self.mergeKLists(lists[:length//2]),self.mergeKLists(lists[length//2:])
        res = ListNode(0)
        curr = res
        while head and tail:
            if head.val < tail.val:
                node = ListNode(head.val)
                head = head.next
            else:
                node = ListNode(tail.val)
                tail = tail.next
            curr.next = node
            curr = node
        if head:
            curr.next = head
        else:
            curr.next = tail
        return res.next
