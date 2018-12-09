'''
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length == 0: return []
        elif length == 1: return [[nums[0]]]
        else:
            res = self.permute(nums[1:])
            ans = []
            for i in range(length):
                for r in res:
                    ans.append(r[:i]+[nums[0]]+r[i:])
            return ans