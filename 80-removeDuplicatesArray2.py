'''
80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
It doesn't matter what values are set beyond the returned length.
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        currNum, currCnt = nums[0], 1
        curr, head = 1, 1
        while(curr < len(nums)):
            print(nums,curr,head, currNum, currCnt)
            if nums[curr] == currNum:
                currCnt += 1
            else:
                currNum = nums[curr]
                currCnt = 1
            if currCnt <= 2:
                if head != curr:
                    nums[head], nums[curr] = nums[curr], nums[head]
                curr += 1
                head += 1
            else:
                curr += 1
        return head

if __name__ == '__main__':
	nums = [1,1,1,2,2,3]
	num = Solution().removeDuplicates(nums)
	print(nums[:num])
