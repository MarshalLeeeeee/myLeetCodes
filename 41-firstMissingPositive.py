'''
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution:
    # very brilliant solution referring to others
    # making one figure in the array represent 2 meanings
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        left = 0
        for i,n in enumerate(nums):
            if n <= 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        nums = nums[left:]
        if not nums:
            return 1
        length = len(nums)
        for i,n in enumerate(nums):
            if abs(n) <= length and nums[abs(n)-1] > 0:
                nums[abs(n)-1] = -nums[abs(n)-1]
        for i,n in enumerate(nums):
            if nums[i] > 0:
                return i+1
        return length+1
        
if __name__ == '__main__':
    print(Solution().firstMissingPositive([2,2]))