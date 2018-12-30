'''
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Return 0 if the array contains less than 2 elements.

Example 1:
Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

Example 2:
Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Note:
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
'''

class Solution:
    # O(n) time and space
    # bucket sort, ever bucket stors the minimum and maximum in the bucket
    # the key idea is that the maximum gap of 'n' numbers with the range [minN, maxN] is greater than (maxN - minN) / (n - 1)
    def init(self,length,n):
        res = []
        for i in range(length):
            res.append(n)
        return res
            
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) < 2: return 0
        minN, maxN,length = float('inf'), float('-inf'), len(nums)
        for n in nums:
            minN = min(minN,n)
            maxN = max(maxN,n)
        gap = maxN - minN
        if not gap: return 0
        step = gap // (length-1) + 1
        minArray, maxArray = self.init(length,float('inf')), self.init(length,float('-inf'))
        for n in nums:
            index = (n-minN) // step
            minArray[index] = min(minArray[index],n)
            maxArray[index] = max(maxArray[index],n)
        res = maxArray[0] - minArray[0]
        lastMax = float('inf')
        for i in range(length):
            if minArray[i] != float('inf'): 
                res= max(res,minArray[i]-lastMax)
                lastMax = maxArray[i]
        return res