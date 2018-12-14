'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

class Solution:
    def getMatrix(self,matrix,index,row,col):
        i = index // col
        j = index - i * col
        return matrix[i][j]
        
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row*col-1
        while(left <= right):
            mid = (left+right) // 2
            midMatrix = self.getMatrix(matrix,mid,row,col)
            if midMatrix < target:
                left = mid + 1
            elif midMatrix > target:
                right = mid - 1
            else:
                return True
        return False