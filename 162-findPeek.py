'''
162. Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:
Your solution should be in logarithmic complexity.
'''

class Solution:
    # O(n) time
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        elif len(nums) == 1: return 0
        else:
            nums.append(float('-inf'))
            nums = [float('-inf')] + nums
            for i in range(1,len(nums)-1):
                if nums[i] > nums[i+1] and nums[i] > nums[i-1]: return i-1


class Solution2:
    # O(logn) time
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return -1
        else:
            left, right = 0, len(nums) - 1
            while left <= right:
                if left == right: return left
                mid = (left + right) // 2
                if left == mid: return left if nums[left] > nums[right] else right
                else:
                    if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]: return mid
                    elif nums[mid] > nums[mid-1]: left = mid
                    elif nums[mid] > nums[mid+1]: right = mid
                    else: left = mid+1

if __name__ == '__main__':
    print(Solution2().findPeakElement([1,2,3,1]))