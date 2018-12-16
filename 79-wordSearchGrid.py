'''
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution:
    def dfs(self, board, visited, word, i, j):
        if not word: return True
        row, col = len(board), len(board[0])
        if i-1 >= 0 and not visited[i-1][j] and board[i-1][j] == word[0]: # up
            visited[i-1][j] = 1
            if self.dfs(board,visited,word[1:],i-1,j): return True
            visited[i-1][j] = 0
        if i+1 < row and not visited[i+1][j] and board[i+1][j] == word[0]: # down
            visited[i+1][j] = 1
            if self.dfs(board,visited,word[1:],i+1,j): return True
            visited[i+1][j] = 0
        if j-1 >= 0 and not visited[i][j-1] and board[i][j-1] == word[0]: # left
            visited[i][j-1] = 1
            if self.dfs(board,visited,word[1:],i,j-1): return True
            visited[i][j-1] = 0
        if j+1 < col and not visited[i][j+1] and board[i][j+1] == word[0]: # right
            visited[i][j+1] = 1
            if self.dfs(board,visited,word[1:],i,j+1): return True
            visited[i][j+1] = 0
        return False
        
    def initVisited(self,row,col):
        res = []
        for i in range(row):
            res.append([])
            for j in range(col):
                res[-1].append(0)
        return res
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word: return True
        elif not board: return False
        else:
            row, col = len(board), len(board[0])
            visited = self.initVisited(row,col)
            for i in range(row):
                for j in range(col):
                    if board[i][j] == word[0]:
                        visited[i][j] = 1
                        if self.dfs(board,visited,word[1:],i,j): return True
                        visited[i][j] = 0
            return False