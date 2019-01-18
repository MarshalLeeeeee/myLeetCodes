'''
234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def init(nums):
	head = ListNode(0)
	curr = head
	for n in nums:
		node = ListNode(n)
		curr.next = node
		curr = curr.next
	return head.next

def show(head):
	curr = head
	while curr:
		print(curr.val,end=' ')
		curr = curr.next
	print('')

class Solution:
	# calculate length first
	# reverse the tail part
	# iterate both the linked list
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head: return True
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if length == 1: return True
        curr, i = head, 0
        while curr:
            if i == length//2-1:
                currNext = curr.next
                curr.next = None
                curr = currNext
                if i == (length+1)//2-1: currPrev = None
            elif i == (length+1)//2-1: currPrev, curr = None,curr.next
            elif i >= (length+1)//2:
                currNext = curr.next
                curr.next = currPrev
                currPrev = curr
                curr = currNext
            else: curr = curr.next
            i += 1
        currh, currt = head, currPrev
        while currh and currt:
            if currh.val != currt.val: return False
            currh = currh.next
            currt = currt.next
        return True

if __name__ == '__main__':
	print(Solution().isPalindrome(init([1,2,1])))