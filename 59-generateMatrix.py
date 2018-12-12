'''
59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

class Solution:
    def init(self, n):
        res = []
        for x in range(n):
            res.append([])
            for y in range(n):
                res[-1].append(0)
        return res
        
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n: return []
        if n == 1: return [[1]]
        res = self.init(n)
        i,j,cnt,direction = 0,0,1,0
        while(cnt <= n*n):
            res[i][j],cnt = cnt,cnt+1
            if direction == 0:
                j += 1
                if j == n or res[i][j]:
                    i,j,direction = i+1,j-1,1
            elif direction == 1:
                i += 1
                if i == n or res[i][j]:
                    i,j,direction = i-1,j-1,2
            elif direction == 2:
                j -= 1
                if j < 0 or res[i][j]:
                    i,j,direction = i-1,j+1,3
            else:
                i -= 1
                if i < 0 or res[i][j]:
                    i,j,direction = i+1,j+1,0
        return res
        