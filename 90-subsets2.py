'''
90. Subsets II

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for n in nums:
            try: dic[n] += 1
            except: dic[n] = 1
        
        ans = [[]]
        for i,k in enumerate(dic):
            add = []
            for a in ans:
                for i in range(1,dic[k]+1):
                    add.append(a+[k]*i)
            ans += add
        return ans
        