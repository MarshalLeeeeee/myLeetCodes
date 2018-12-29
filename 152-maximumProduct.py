'''
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')
        maxTail, minTail = 1, 1
        for n in nums:
            res = max(res,n*maxTail,n*minTail)
            maxTail, minTail = max(1, n*maxTail, n*minTail), min(1, n*maxTail, n*minTail)
        return res