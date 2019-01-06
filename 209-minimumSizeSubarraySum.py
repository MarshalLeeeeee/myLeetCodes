'''
209. Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
'''

class Solution:
    # O(n^2) time limit exceed
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sums, ans = [], float('inf')
        for i in range(len(nums)):
            sums.append(0)
            for si in range(len(sums)-1,-1,-1):
                sums[si] += nums[i]
                if sums[si] >= s: 
                    ans = min(ans,len(sums)-si)
                    sums = sums[si+1:]
                    break
        return 0 if ans == float('inf') else ans

class Solution2:
    # O(nlogn) solution
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        sums, ans = [nums[0]], float('inf')
        for i in range(1,len(nums)):
            sums.append(sums[i-1]+nums[i])
        gap = 0
        for si in range(len(sums)):
            # find the minimal sum >= s
            left, right = si, len(sums)-1
            while left <= right:
                mid = (left+right) // 2
                if sums[mid] - gap > s: right = mid - 1
                elif sums[mid] - gap < s: left = mid + 1
                else: xi = mid; break
            if left > right: xi = left
            if xi != len(sums): ans = min(ans,xi-si+1)
            gap = sums[si]
        return 0 if ans == float('inf') else ans




if __name__ == '__main__':
    print(Solution2().minSubArrayLen(7,[2,3,1,2,4,3]))