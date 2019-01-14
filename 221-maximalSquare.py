'''
221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
'''

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        row, col, res = len(matrix), len(matrix[0]), 0
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1': 
                    if not res: res = 1
                    if not i and not j: matrix[i][j] = [1,1,1]
                    elif not i: matrix[i][j] = [matrix[i][j-1][0]+1,1,1]
                    elif not j: matrix[i][j] = [1,matrix[i-1][j][1]+1,1]
                    else: 
                        matrix[i][j] = [matrix[i][j-1][0]+1,matrix[i-1][j][1]+1]
                        matrix[i][j].append(min(matrix[i][j][0], matrix[i][j][1],matrix[i-1][j-1][2]+1))
                        res = max(res,matrix[i][j][2])
                else: matrix[i][j] = [0,0,0]
        return res*res