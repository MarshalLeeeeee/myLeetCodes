'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def binarySearch(self, nums, target, start, end):
        # find exactly the target
        while(start <= end):
            mid = (start+end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        return -1
    
    def binarySearchBigger(self, nums, target, start, end):
        # find the smallest index which is bigger than the target
        while(start <= end):
            mid = (start+end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid -1
        return start
        
    def binarySearchSmaller(self, nums, target, start, end):
        # find the biggest index which is smaller than the target
        while(start <= end):
            mid = (start+end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return end
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = -1, -1
        if not nums:
            return [left, right]
        targetIndex = self.binarySearch(nums,target,0,len(nums)-1)
        if targetIndex == -1:
            return [left,right]
        left = self.binarySearchBigger(nums,target-1,0,targetIndex)
        right = self.binarySearchSmaller(nums,target+1,targetIndex,len(nums)-1)
        return [left,right]
        
if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10],8))