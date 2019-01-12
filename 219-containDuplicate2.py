'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] 
and the absolute difference between i and j is at most k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

class Solution:
    # record every index for every appeared number
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums: return False
        dic = {}
        for i,n in enumerate(nums):
            if n not in dic: dic[n] = [i]
            else: dic[n].append(i)
        for key in dic:
            if len(dic[key]) != 1:
                for i in range(1,len(dic[key])):
                    if dic[key][i] - dic[key][i-1] <= k: return True
        return False

class Solution2:
    # record the last position of every having appeared number
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums: return False
        dic = {}
        for i,n in enumerate(nums):
            if n not in dic: dic[n] = i
            else: 
                if i - dic[n] <= k: return True
                else: dic[n] = i
        return False