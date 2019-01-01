class Solution:
    # dp from leftup to rightbottom
    # logical feasible
    # time limit exceed
    def init(self,row,col):
        res = []
        for i in range(row):
            res.append([])
            for j in range(col):
                res[-1].append(0)
        return res
        
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        row, col = len(dungeon), len(dungeon[0])
        res = self.init(row,col)
        res[0][0] = [[-dungeon[0][0],max(0,-dungeon[0][0])]]
        for i in range(1,row):
            res[i][0] = [[res[i-1][0][0][0]-dungeon[i][0],max(res[i-1][0][0][0]-dungeon[i][0],res[i-1][0][0][1])]]
        for j in range(1,col):
            res[0][j] = [[res[0][j-1][0][0]-dungeon[0][j],max(res[0][j-1][0][0]-dungeon[0][j],res[0][j-1][0][1])]]
        for i in range(1,row):
            for j in range(1,col):
                tmp = []
                minN, min0 = float('inf'), float('inf')
                for x in res[i-1][j]+res[i][j-1]:
                    r = [x[0] - dungeon[i][j],max(x[0] - dungeon[i][j],x[1])]
                    if r[1] <= minN: 
                        min0 = min(min0,r[0]) if r[1] == minN else r[0]
                        minN = r[1]
                    tmp.append(r) 
                tmp2 = []
                for t in tmp:
                    if t[0] <= min0: tmp2.append(t)
                res[i][j] = tmp2
        minN = float('inf')
        for r in res[-1][-1]:
            minN = min(minN,r[1])
        return minN+1

class Solution2:
    # dp from rightbottom to leftup
    # slightly simpler and faster than solution1
    # the reason is 
    #       by solution2, the partial result is always the answer of the current place to the terminal (which is easy to calculate)
    # while by solution1, the partial result is the answer of the start to the current place (which is the peek value and header to calculate)
    def calculateMinimumHP(self, dungeon):
        m,n = len(dungeon),len(dungeon[0])
        dungeon[m-1][n-1] = -dungeon[m-1][n-1] if dungeon[m-1][n-1] < 0 else 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1: continue
                dungeon[i][j] = min((dungeon[i+1][j] if i+1 < m else float('inf')), (dungeon[i][j+1] if j+1 < n else float('inf'))) - dungeon[i][j] 
                if dungeon[i][j] < 0: dungeon[i][j] = 0  
        return dungeon[0][0] + 1