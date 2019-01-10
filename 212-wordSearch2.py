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

#####################################################################################################################################

# use the alphabet tree
# dfs by tracking the pos in the board
# calculate the every possible route for every prefix in the tree
#     many synchronized dfs
#     thus no pruning is performed and 
class wordTree:
    def __init__(self):
        self.root = [{},[],[]]
    
    def add(self,word):
        curr = self.root
        for w in word:
            if w not in curr[0]: curr[0][w] = [{},[],[]]
            curr = curr[0][w]
        curr[0][''] = [{},[],[]]
        
    def __dfs__(self,board,row,col,curr,prefix,res):
        if '' in curr[0]: res.add(prefix)
        for i in range(len(curr[2])):
            path = curr[1][i]
            pos = curr[2][i]
            x, y = pos//col, pos%col
            #print(row,col,i,x,y,path,prefix)
            if x > 0 and (x-1)*col+y not in path and board[x-1][y] in curr[0] and prefix+board[x-1][y] not in res: 
                curr[0][board[x-1][y]][1].append(path | set([(x-1)*col+y]))
                curr[0][board[x-1][y]][2].append((x-1)*col+y)
                self.__dfs__(board,row,col,curr[0][board[x-1][y]],prefix+board[x-1][y],res)
            if y > 0 and x*col+(y-1) not in path and board[x][y-1] in curr[0] and prefix+board[x][y-1] not in res: 
                curr[0][board[x][y-1]][1].append(path | set([x*col+(y-1)]))
                curr[0][board[x][y-1]][2].append(x*col+(y-1))
                self.__dfs__(board,row,col,curr[0][board[x][y-1]],prefix+board[x][y-1],res)
            if x < row-1 and (x+1)*col+y not in path and board[x+1][y] in curr[0] and prefix+board[x+1][y] not in res: 
                curr[0][board[x+1][y]][1].append(path | set([(x+1)*col+y]))
                curr[0][board[x+1][y]][2].append((x+1)*col+y)
                self.__dfs__(board,row,col,curr[0][board[x+1][y]],prefix+board[x+1][y],res)
            if y < col-1 and x*col+(y+1) not in path and board[x][y+1] in curr[0] and prefix+board[x][y+1] not in res: 
                curr[0][board[x][y+1]][1].append(path | set([x*col+(y+1)]))
                curr[0][board[x][y+1]][2].append(x*col+(y+1))
                self.__dfs__(board,row,col,curr[0][board[x][y+1]],prefix+board[x][y+1],res)
            
        
    def dfs(self,board):
        row, col, curr = len(board), len(board[0]), self.root
        for i in range(row):
            for j in range(col):
                if board[i][j] in self.root[0]: 
                    self.root[0][board[i][j]][1].append(set([i*col+j]))
                    self.root[0][board[i][j]][2].append(i*col+j)
        res = set()
        for c in self.root[0]:
            if self.root[0][c][1]: 
                print(self.root[0][c][1])
                print(self.root[0][c][2])
                self.__dfs__(board,row,col,self.root[0][c],c,res)
        return list(res)

class Solution2:        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row, col = len(board), len(board[0])
        wt = wordTree()
        for w in words:
            if len(w) <= row*col: wt.add(w)
        return wt.dfs(board)

############################################################################################################################

# use alphabet tree
# mapping the original 2-d board into single value set
# dfs through the alphabet tree by managing the set
class wordTree:
    def __init__(self):
        self.root = {}
        self.map = {}
        self.row = -1
        self.col = -1
    
    def add(self,word):
        curr = self.root
        for w in word:
            if w not in curr: curr[w] = {}
            curr = curr[w]
        curr[''] = {}
        
    def load(self,board):
        self.row, self.col = len(board), len(board[0])
        for i in range(self.row):
            for j in range(self.col):
                c = board[i][j]
                if c not in self.map: self.map[c] = set([i*(self.col+2)+j+1])
                else: self.map[c].add(i*(self.col+2)+j+1)
        
    def __dfs__(self,curr,pos,path,res):
        for child in curr:
            if child == '': 
                res.add(path)
            else:
                if child in self.map:
                    if pos+1 in self.map[child]:
                        self.map[child].remove(pos+1)
                        self.__dfs__(curr[child],pos+1,path+child,res)
                        self.map[child].add(pos+1)
                    if pos-1 in self.map[child]:
                        self.map[child].remove(pos-1)
                        self.__dfs__(curr[child],pos-1,path+child,res)
                        self.map[child].add(pos-1)
                    if pos-(self.col+2) in self.map[child]:
                        self.map[child].remove(pos-(self.col+2))
                        self.__dfs__(curr[child],pos-(self.col+2),path+child,res)
                        self.map[child].add(pos-(self.col+2))
                    if pos+(self.col+2) in self.map[child]:
                        self.map[child].remove(pos+(self.col+2))
                        self.__dfs__(curr[child],pos+(self.col+2),path+child,res)
                        self.map[child].add(pos+(self.col+2))
        
    def dfs(self):
        res = set()
        for child in self.root:
            if child in self.map: 
                position = self.map[child].copy()
                for pos in position:
                    self.map[child].remove(pos)
                    self.__dfs__(self.root[child],pos,child,res)
                    self.map[child].add(pos)
        return list(res)

class Solution3:        
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row, col = len(board), len(board[0])
        wt = wordTree()
        for w in words:
            if len(w) <= row*col: wt.add(w)
        wt.load(board)
        return wt.dfs()
    
if __name__ == '__main__':
    print(Solution().findWords([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]],["aaaaaaaaaaaa","aaaaaaaaaaaaa","aaaaaaaaaaab"]))