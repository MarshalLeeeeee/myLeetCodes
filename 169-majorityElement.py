'''
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = []
        for n in nums:
            if not m: m.append([n,1])
            else:
                if n == m[0][0]: m[0][1] += 1
                else: 
                    m[0][1] -= 1
                    if not m[0][1]: m.pop()
        return m[0][0]