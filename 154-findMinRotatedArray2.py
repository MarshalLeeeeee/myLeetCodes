'''
154. Find Minimum in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2: 
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if left == right or nums[left] < nums[right]: return nums[left]
            elif nums[mid] > nums[right]: left = mid+1
            elif nums[mid] < nums[left]: right = mid
            else:
                i = left+1
                while i < right:
                    if nums[i] < nums[left]: return nums[i]
                    elif nums[i] > nums[left]: break
                    i += 1
                left = i

if __name__ == '__main__':
    print(Solution().findMin([1,1,1]))
            