'''
77. Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k: return []
        if k == 1:
            return [[x] for x in range(1,n+1)]
        ans1 = self.combine(n-1,k)
        ans2 = self.combine(n-1,k-1)
        for a in ans2:
            a.append(n)
        return ans1+ans2

if __name__ == '__main__':
    print(Solution().combine(4,3))