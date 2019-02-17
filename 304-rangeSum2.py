'''
304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''

class NumMatrix:
    def __init__(self, matrix: 'List[List[int]]'):
        self.sum = []
        if matrix: self.row, self.col = len(matrix), len(matrix[0])
        else: self.row, self.col = 0, 0
        for i in range(self.row):
            self.sum.append([])
            if not i: s = 0
            for j in range(self.col):
                if not i and not j: self.sum[i].append(matrix[i][j])
                elif not i: self.sum[i].append(matrix[i][j]+self.sum[i][j-1])
                elif not j: self.sum[i].append(matrix[i][j]+self.sum[i-1][j])
                else: self.sum[i].append(matrix[i][j]+self.sum[i-1][j]+self.sum[i][j-1]-self.sum[i-1][j-1])

    def sumRegion(self, row1: 'int', col1: 'int', row2: 'int', col2: 'int') -> 'int':
        if not row1 and not col1: return self.sum[row2][col2]
        elif not row1: return self.sum[row2][col2] - self.sum[row2][col1-1]
        elif not col1: return self.sum[row2][col2] - self.sum[row1-1][col2]
        else: return self.sum[row2][col2] - self.sum[row1-1][col2] - self.sum[row2][col1-1] + self.sum[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)