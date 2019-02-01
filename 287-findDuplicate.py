'''
287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
'''

class Solution:
    # O(bucket) space, where bucket is a constant
    # O(n^2) time
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        bucket = 10000
        passes = (length-1) // bucket + 1
        index = 0
        while index < passes:
            record = [0] * bucket
            for n in nums:
                if index*bucket < n and n <= (index+1)*bucket:
                    if record[(n-1)%bucket]: return n
                    record[(n-1)%bucket] += 1 
            index += 1



if __name__ == '__main__':
    print(Solution3().findDuplicate([1,3,4,2,2]))