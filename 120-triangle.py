'''
120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''

class Solution:
    # O(col) space
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        col = len(triangle)
        if not col: return 0
        elif col == 1: return triangle[0][0]
        else:
            pre = triangle[0]
            for i in range(1,col):
                curr = []
                for j in range(i+1):
                    if not j: curr.append(pre[j]+triangle[i][j])
                    elif j == i: curr.append(pre[j-1]+triangle[i][j])
                    else: curr.append(min(pre[j-1],pre[j])+triangle[i][j])
                pre = curr
            minNum = curr[0]
            for c in curr[1:]:
                if c < minNum: minNum = c
            return minNum