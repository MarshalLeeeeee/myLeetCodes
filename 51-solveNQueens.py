class Solution:
    # feasible in logic
    # but search can be optimized (to Solution2)
    def isValid(self,board,n,i,j):
        for x in range(n):
            if board[i][x] or board[x][j]: return False
        for x in range(n):
            y = j-i+x
            z = j+i-x
            if (y >= 0 and y < n and board[x][y]) or (z >= 0 and z < n and board[x][z]): return False
        return True
    
    def solve(self,board,visited,ans,n,left):
        if not left:
            record = []
            for x in range(n):
                s = ''
                for y in range(n):
                    s += 'Q' if board[x][y] else '.'
                record.append(s)
            if record not in ans:
                ans.append(record)
        else:
            for x in range(n):
                for y in range(n):
                    if not visited[x][y] and self.isValid(board,n,x,y):
                        board[x][y] = 1
                        visited[x][y] = 1
                        self.solve(board,visited,ans,n,left-1)
                        visited[x][y] = 0
                        board[x][y] = 0

    def init(self,n):
        res = []
        for x in range(n):
            res.append([])
            for y in range(n):
                res[x].append(0)
        return res
            
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = self.init(n)
        visited = self.init(n)
        ans = []
        self.solve(board,visited,ans,n,n)
        return ans

class Solution2:
    def isValid(self,board,n,i,j):
        for x in range(n):
            if board[i][x] or board[x][j]: return False
        for x in range(n):
            y = j-i+x
            z = j+i-x
            if (y >= 0 and y < n and board[x][y]) or (z >= 0 and z < n and board[x][z]): return False
        return True
    
    def solve(self,board,ans,n,row):
        if row == n:
            record = []
            for x in range(n):
                s = ''
                for y in range(n):
                    s += 'Q' if board[x][y] else '.'
                record.append(s)
            if record not in ans:
                ans.append(record)
        else:
            for y in range(n):
                if self.isValid(board,n,row,y):
                    board[row][y] = 1
                    self.solve(board,ans,n,row+1)
                    board[row][y] = 0

    def init(self,n):
        res = []
        for x in range(n):
            res.append([])
            for y in range(n):
                res[x].append(0)
        return res
            
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = self.init(n)
        ans = []
        self.solve(board,ans,n,0)
        return ans

if __name__ == '__main__':
    print(Solution2().solveNQueens(4))