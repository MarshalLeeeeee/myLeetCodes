'''
33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if not length:
            return -1
        left, right = 0, length-1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[right] == target:
                return right
            elif nums[left] == target:
                return left
            if nums[mid] > nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                    right -= 1
                else:
                    if target > nums[right]:
                        left += 1
                        right = mid - 1
                    else:
                        left = mid + 1
                        right -= 1
            else:
                if target < nums[mid]:
                    right = mid - 1
                    left += 1
                else:
                    if target > nums[right]:
                        right = mid - 1
                        left += 1
                    else:
                        left = mid + 1
                        right -= 1
        return -1