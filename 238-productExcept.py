'''
238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class TreeNode:
    def __init__(self,val=float('inf')):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    # tree structure solution
    # merely pass the time limit
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        root = TreeNode()
        root.left = TreeNode(nums[1])
        root.right = TreeNode(nums[0])
        m = nums[0]*nums[1]
        for i in range(2,len(nums)):
            node = TreeNode()
            root.val = nums[i]
            node.left = root
            node.right = TreeNode(m)
            m *= nums[i]
            root = node
        root.val = 1
        curr,res,base = root,[],1
        while True:
            base *= curr.val
            if not curr.right: return [base]+res
            else: res = [base*curr.right.val]+res
            curr = curr.left
        return res


