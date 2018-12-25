'''
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
'''

class Solution:
    # O(n) space
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic, s1, s2 = {}, 0, 0
        for n in nums:
            s1 += n
        nums = set(nums)
        for n in nums:
            s2 += n
        return 2 * s2 - s1
        
class Solution2:
    # O(1) space
    # a XOR 0 = a
    # a XOR a = 0
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res ^= n
        return res