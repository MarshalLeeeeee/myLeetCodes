'''
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

class Solution:
    # O(n) space
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        res = nums[-k:]+nums[:-k]
        for i in range(len(nums)):
            nums[i] = res[i]

class Solution2:
    # O(1) space with recursion
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if not k or not nums: return 
        do = min(k,1000)
        tail = nums[-do:]
        for i in range(len(nums)-1,do-1,-1):
            nums[i] = nums[i-do]
        for i in range(do):
            nums[i] = tail[i]
        self.rotate(nums,k-do)

class Solution3:
    # O(1) space
    # single pass
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if not k or not nums: return 
        i, curr, l = 0, nums[0], len(nums)
        for cnt in range(l):
            if cnt * k % l == 0:
                curr = nums[i+1]
                nextI = (i+1+k) % l
                val = nums[nextI]
                nums[nextI] = curr
                curr, i = val, nextI
            else:
                nextI = (i+k) % l
                val = nums[nextI]
                nums[nextI] = curr
                curr, i = val, nextI