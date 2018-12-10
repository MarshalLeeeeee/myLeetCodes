'''
52. N-Queens II

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''

class Solution:
    def init(self,n):
        res = []
        for i in range(n):
            res.append([])
            for j in range(n):
                res[-1].append(0)
        return res
    
    def isValid(self,board,n,i,j):
        for x in range(n):
            if board[i][x] or board[x][j]: return False
        for x in range(n):
            y = j-i+x
            z = j+i-x
            if (y >= 0 and y < n and board[x][y]) or (z >= 0 and z < n and board[x][z]): return False
        return True
    
    def solve(self,board,ans,n,row):
        if n == row:
            res = []
            for r in board:
                res += r
            if r not in ans:
                ans.append(res)
        else:
            x = row
            for y in range(n):
                if self.isValid(board,n,x,y):
                    board[x][y] = 1
                    self.solve(board,ans,n,row+1)
                    board[x][y] = 0
        
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        board = self.init(n)
        ans = []
        self.solve(board,ans,n,0)
        return len(ans)
        
        