'''
88. Merge Sorted Array

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
'''

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if not m: 
            for i in range(n):
                nums1[i] = nums2[i]
        elif not n: pass
        else:
            mi, ni = 0, 0
            move = []
            while ni < n and mi < m:
                if nums1[mi] < nums2[ni]:
                    move.append(ni)
                    mi += 1
                else:
                    ni += 1
            if len(move) != m:
                for i in range(len(move),m):
                    move.append(ni)
            done = []
            for i in range(m+n):
                done.append(0)
            for i in range(m-1,-1,-1):
                nums1[i], nums1[i+move[i]] = nums1[i+move[i]], nums1[i]
                done[i+move[i]] = 1
            ni = 0
            for i in range(m+n):
                if not done[i]:
                    nums1[i] = nums2[ni]
                    ni += 1