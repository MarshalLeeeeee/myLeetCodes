'''
212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Example:
Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Output: ["eat","oath"]

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

################################################################################################################################

class Solution:
    # naive dfs search
    # we can optimize it by eliminating multiple serach for the same prefix
    def dfs(self,board,visited,row,col,x,y,res,w,i):
        if i == len(w): res.add(w)
        else:
            visited[x][y] = 1
            if x > 0 and board[x-1][y] == w[i] and not visited[x-1][y]: self.dfs(board,visited,row,col,x-1,y,res,w,i+1)
            if y > 0 and board[x][y-1] == w[i] and not visited[x][y-1]: self.dfs(board,visited,row,col,x,y-1,res,w,i+1)
            if x < row-1 and board[x+1][y] == w[i] and not visited[x+1][y]: self.dfs(board,visited,row,col,x+1,y,res,w,i+1)
            if y < col-1 and board[x][y+1] == w[i] and not visited[x][y+1]: self.dfs(board,visited,row,col,x,y+1,res,w,i+1)
            visited[x][y] = 0
        
    def init(self,row,col):
        v = []
        for i in range(row):
            v.append([0]*col)
        return v
        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words: return []
        row,col = len(board), len(board[0])
        words, res = set(words), set([])
        for w in words:
            print(w)
            visited = self.init(row,col)
            for i in range(row):
                for j in range(col):
                    if board[i][j] == w[0]:
                        self.dfs(board,visited,row,col,i,j,res,w,1)
        return list(res)


    
if __name__ == '__main__':
    print(Solution().findWords([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]))