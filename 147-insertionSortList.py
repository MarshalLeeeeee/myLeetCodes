'''
147. Insertion Sort List

Sort a linked list using insertion sort.

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

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
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        newHead = ListNode(0)
        newHead.next = head
        currPrev, curr = head, head.next
        while curr:
            print('-'*10)
            show(newHead.next)
            print('currPrev & curr: ', currPrev.val, curr.val)
            curr2, currPrev2 = newHead.next, newHead
            currNext = curr.next
            while curr2 != curr:
                print('currPrev2 & curr2: ', currPrev2.val, curr2.val)
                if curr2.val > curr.val:
                    curr.next = curr2
                    currPrev2.next = curr
                    currPrev.next = currNext
                    break
                currPrev2, curr2 = curr2, curr2.next
            if curr2 == curr: currPrev = curr
            curr = currNext
        return newHead.next

def init(nums):
    head = ListNode(0)
    prev = head
    for n in nums:
        node = ListNode(n)
        prev.next = node
        prev = node
    return head.next

def show(head):
    curr = head
    print('show:',end='')
    while curr:
        print(curr.val,end=',')
        curr = curr.next
    print('')

if __name__ == '__main__':
    l = init([4,2,1,3])
    res = Solution().insertionSortList(l)
    show(res)