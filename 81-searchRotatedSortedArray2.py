'''
81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''

class Solution:
    # when duplicate exists, worst case is O(n)
    # average O(logn)
    def findNonduplicate(self, nums, target, left, right):
        if left > right: return left,right,-1
        mid = (left+right) // 2
        if nums[mid] != target: return left,right,mid
        else:
            lLeft, lRight, lMid = self.findNonduplicate(nums,target,left,mid-1)
            rLeft, rRight, rMid = self.findNonduplicate(nums,target,mid+1,right)
            if lMid != -1: return lLeft, lRight, lMid
            elif rMid != -1: return rLeft, rRight, rMid
            else: return left,right,-1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums: return False
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > nums[right]: # pivot at the right part
                if target > nums[mid]: left = mid + 1
                elif target < nums[mid]:
                    if target > nums[right]: right = mid - 1
                    elif target < nums[right]: left = mid + 1
                    else: return True
                else: return True
            elif nums[mid] < nums[right]: # pivot at the left part
                if target < nums[mid]: right = mid - 1
                elif target > nums[mid]:
                    if target > nums[right]: right = mid - 1
                    elif target < nums[right]: left = mid + 1
                    else: return True
                else: return True
            else:
                if nums[mid] == target: return True
                else:
                    if mid == 0: break
                    else:
                        newLeft, newRight, rMid = self.findNonduplicate(nums,nums[mid],left,right)
                        if rMid == -1: return False
                        else: left, right = newLeft, newRight 
        return False
