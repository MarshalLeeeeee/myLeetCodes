'''
62. Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
'''

class Solution:
    def init(self,m,n):
        res = []
        for i in range(m):
            res.append([])
            for j in range(n):
                if i == 0 or j == 0: res[-1].append(1)
                else: res[-1].append(0)
        return res
                
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = self.init(m,n)
        for i in range(1,m):
            for j in range(1,n):
                if not res[i][j]: res[i][j] = res[i-1][j] + res[i][j-1]
        return res[m-1][n-1]