'''
137. Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
'''

class Solution(object):
    # O(n) space
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic, dupSet = {}, set([])
        for n in nums:
            try: 
                dic[n] += 1
                dupSet |= set([n])
            except: dic[n] = 1
        res = list(set(nums) - dupSet)
        return res[0]

class Solution(object):
    # O(1) space
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two = 0, 0
        for n in nums:
            # either one or two can be not 0
            # three state loop
            one = (one ^ n) & ~two
            two = (two ^ n) & ~one
        return one