'''
130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

class Solution:
    # dfs solution
    # start from edge
    def init(self,board,row,col):
        res = []
        for i in range(row):
            res.append([])
            for j in range(col):
                if board[i][j] == 'O': res[-1].append(0)
                else: res[-1].append(1)
        return res
    
    def dfs(self,visited,i,j,row,col):
        if i != 0 and not visited[i-1][j]:
            visited[i-1][j] = 1
            self.dfs(visited,i-1,j,row,col)
        if j != 0 and not visited[i][j-1]:
            visited[i][j-1] = 1
            self.dfs(visited,i,j-1,row,col)
        if i != row-1 and not visited[i+1][j]:
            visited[i+1][j] = 1
            self.dfs(visited,i+1,j,row,col)
        if j != col-1 and not visited[i][j+1]:
            visited[i][j+1] = 1
            self.dfs(visited,i,j+1,row,col)
        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board:
            row, col = len(board), len(board[0])
            visited = self.init(board,row,col)
            for i in range(row):
                if not visited[i][0]:
                    visited[i][0] = 1
                    self.dfs(visited,i,0,row,col)
                if not visited[i][col-1]:
                    visited[i][col-1] = 1
                    self.dfs(visited,i,col-1,row,col)
                    
            for j in range(col):
                if not visited[0][j]:
                    visited[0][j] = 1
                    self.dfs(visited,0,j,row,col)
                if not visited[row-1][j]:
                    visited[row-1][j] = 1
                    self.dfs(visited,row-1,j,row,col)
                    
            for i in range(row):
                for j in range(col):
                    if board[i][j] == 'O' and not visited[i][j]: board[i][j] = 'X'