class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return matrix
        row, col = len(matrix), len(matrix[0])
        
        rowFlag, colFlag = False, False
        if not matrix[0][0]:
            rowFlag, colFlag = True, True
        else:
            for i in range(1,row):
                if not matrix[i][0]:
                    colFlag = True
                    break
            for j in range(1,col):
                if not matrix[0][j]:
                    rowFlag = True
                    break
                    
        for i in range(1,row):
            for j in range(1,col):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,row):
            if not matrix[i][0]:
                for j in range(1,col):
                    matrix[i][j] = 0
                    
        for j in range(1,col):
            if not matrix[0][j]:
                for i in range(1,row):
                    matrix[i][j] = 0
        
        if rowFlag:
            for j in range(col):
                matrix[0][j] = 0
        
        if colFlag:
            for i in range(row):
                matrix[i][0] = 0

if __name__ == '__main__':
    matrix = [[1,0,3]]
    Solution().setZeroes(matrix)
    print(matrix)