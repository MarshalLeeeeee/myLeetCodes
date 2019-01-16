'''
229. Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a,b = [float('-inf'),0],[float('-inf'),0]
        for n in nums:
            if n == a[0]: a[1] += 1
            elif n == b[0]: b[1] += 1
            elif not a[1]: a = [n,1]
            elif not b[1]: b = [n,1]
            else: a[1], b[1] = a[1]-1, b[1]-1
        res, bound = [], len(nums)//3
        if a[1]: 
            cnt = 0
            for n in nums:
                if n == a[0]: cnt += 1
            if cnt > bound: res.append(a[0])
        if b[1]: 
            cnt = 0
            for n in nums:
                if n == b[0]: cnt += 1
            if cnt > bound: res.append(b[0])
        return res