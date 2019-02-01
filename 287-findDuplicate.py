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

class Solution2:
    # O(n) time and O(1) space
    # treat the array as list, noticed that the range of numbers are within [1,n]
    # since the linked list start from 'nums[0]' and 0 in not within the 
    # Lemma: the linked list will contain a loop where the intersection node is the duplicate one iff. the array contains one duplicate number 
    #    =>
    #       Notice that the intersection of the loop cannot be the first node because 0 is not within the range of the number
    #       Thus, the intersection number will have two different numbers as prefix which denotes two distinct index in the original array, which proves it as the duplicate number
    #       For those single number, since they appear at certain index, they have only one prefix in the linked list
    #    <=
    #       Since the linked list can be continuously visited the next element, it is either infinite or has a loop
    #       However, the number is finite which is within [1,n], there must be a loop in the linked list
    #       The intersection node will have two different prefix node, which means the duplicate number will be certainly contained in the loop linked list
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast, slow = nums[0], nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

class Solution3:
    # O(nlogn) time and O(1) space
    # binary search for [1,n] within which one is the answer
    # in every search, traverse all nums
    # as long as that the number > range, the answer is within the range
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        left, right = 1, length-1
        while left < right:
            cntLeft, cntRight, mid = 0, 0, (left+right) // 2
            for n in nums:
                if left <= n and n <= mid: cntLeft += 1
                if mid < n and n <= right: cntRight += 1
            if cntLeft > mid - left + 1: right = mid
            elif cntRight > right - mid: left = mid + 1
        return left

if __name__ == '__main__':
    print(Solution3().findDuplicate([1,3,4,2,2]))