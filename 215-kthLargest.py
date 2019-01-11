'''
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution:   
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot, lp = nums[0], 1
        for i in range(1,len(nums)):
            if nums[i] <= pivot: break
            else: lp += 1
        for i in range(lp+1,len(nums)):
            if nums[i] > pivot: nums[lp],nums[i] = nums[i],nums[lp]; lp += 1
        if k > lp: return self.findKthLargest(nums[lp:],k-lp)
        elif k < lp: return self.findKthLargest(nums[1:lp],k)
        else: return pivot

class Solution2:   
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]