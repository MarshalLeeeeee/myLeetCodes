'''
109. Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursion using whoes input is list
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head:
            length,curr = 0,head
            while curr:
                length += 1
                curr = curr.next
            cnt, curr, currPrev = 0, head, None
            while curr:
                if cnt == length // 2:
                    root = TreeNode(curr.val)
                    if currPrev: 
                        currPrev.next = None
                        root.left = self.sortedListToBST(head)
                    root.right = self.sortedListToBST(curr.next)
                curr, currPrev = curr.next, curr
                cnt += 1
            return root
        
class Solution2:
    # convert list to array
    # then input array
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums,curr = [],head
        while curr:
            nums.append(curr.val)
            curr = curr.next
        return self.sortedArrayToBST(nums)


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            l = len(nums)
            root = TreeNode(nums[l//2])
            root.left = self.sortedArrayToBST(nums[:l//2])
            root.right = self.sortedArrayToBST(nums[l//2+1:])
            return root