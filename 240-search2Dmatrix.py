'''
240. Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
'''

class Solution:    
    def solve(self,xl,yl,xr,yr,row,col,matrix,target):
        if xl == row or yl == col: return False
        xDelta,yDelta = xr-xl, yr-yl
        if not xDelta:
            l,r = yl, yr
            while l <= r:
                mid = (l+r) // 2
                if matrix[xl][mid] > target: r = mid - 1
                elif matrix[xl][mid] < target: l = mid + 1
                else: return True
            return False
        elif not yDelta:
            l,r = xl, xr
            while l <= r:
                mid = (l+r) // 2
                if matrix[mid][yl] > target: r = mid - 1
                elif matrix[mid][yl] < target: l = mid + 1
                else: return True
            return False
        else:
            delta = min(xDelta,yDelta)
            l, r = 0, delta
            while l <= r:
                mid  = (l+r) // 2
                if matrix[xl+mid][yl+mid] > target: r = mid - 1
                elif matrix[xl+mid][yl+mid] < target: l = mid + 1
                else: return True
            if r < 0: return False
            return self.solve(xl+r+1,yl,xr,yl+r,row,col,matrix,target) or self.solve(xl,yl+r+1,xl+r,yr,row,col,matrix,target)
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        xl, xr = 0, len(matrix)-1
        yl, yr = 0, len(matrix[0])-1
        row, col = xr+1, yr+1
        return self.solve(xl,yl,xr,yr,row,col,matrix,target)

if __name__ == '__main__':
    matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    target = 15
    print(Solution().searchMatrix(matrix,target))