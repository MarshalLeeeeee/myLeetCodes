'''
48. Rotate Image

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        if matrix and length != 1:
            if length % 2 == 0:
                center = length // 2 - 0.5
                for i in range(length//2):
                    for j in range(length//2):
                        x1,y1 = int(center-0.5-i),int(center-0.5-j)
                        x2,y2 = int(center-0.5-j),int(center+0.5+i)
                        x3,y3 = int(center+0.5+i),int(center+0.5+j)
                        x4,y4 = int(center+0.5+j),int(center-0.5-i)
                        matrix[x1][y1],matrix[x2][y2],matrix[x3][y3],matrix[x4][y4] = matrix[x4][y4],matrix[x1][y1],matrix[x2][y2],matrix[x3][y3]
            else:
                center = length // 2
                for i in range(center+1):
                    for j in range(1,center+1):
                        x1,y1 = center-i,center-j
                        x2,y2 = center-j,center+i
                        x3,y3 = center+i,center+j
                        x4,y4 = center+j,center-i
                        matrix[x1][y1],matrix[x2][y2],matrix[x3][y3],matrix[x4][y4] = matrix[x4][y4],matrix[x1][y1],matrix[x2][y2],matrix[x3][y3]