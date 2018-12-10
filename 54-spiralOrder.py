'''
54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def init(self, h, w):
        res = []
        for x in range(h):
            res.append([])
            for y in range(w):
                res[-1].append(0)
        return res
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        direction, i, j, cnt, ans = 0, 0, 0, 0, []
        height, width = len(matrix), len(matrix[0])
        visited = self.init(height,width)
        while True:
            ans.append(matrix[i][j])
            visited[i][j], cnt = 1, cnt + 1
            if cnt == height * width: return ans
            if direction == 0:
                j += 1
                if j >= width or visited[i][j]:
                    j,i,direction = j-1, i+1, 1
            elif direction == 1:
                i += 1
                if i >= height or visited[i][j]:
                    i,j,direction = i-1,j-1,2
            elif direction == 2:
                j -= 1
                if j < 0 or visited[i][j]:
                    j,i,direction = j+1, i-1, 3
            else:
                i -= 1
                if i < 0 or visited[i][j]:
                    i,j,direction = i+1, j+1, 0
            