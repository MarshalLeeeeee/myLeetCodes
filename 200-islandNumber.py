'''
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''

class Solution:
    def dfs(self,grid,row,col,i,j):
        grid[i][j] = '0'
        if i > 0 and grid[i-1][j] == '1': self.dfs(grid,row,col,i-1,j)
        if j > 0 and grid[i][j-1] == '1': self.dfs(grid,row,col,i,j-1)
        if i < row-1 and grid[i+1][j] == '1': self.dfs(grid,row,col,i+1,j)
        if j < col-1 and grid[i][j+1] == '1': self.dfs(grid,row,col,i,j+1)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        if not grid: return 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    cnt += 1
                    self.dfs(grid,row,col,i,j)
        return cnt