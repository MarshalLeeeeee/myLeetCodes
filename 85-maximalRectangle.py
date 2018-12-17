'''
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

class Solution:
    # based on problem 84
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        stack, index, maxArea = [], 0, 0
        while index < len(heights):
            if not stack: stack.append((heights[index],index))
            else:
                if heights[index] > stack[-1][0]: stack.append((heights[index],index))
                elif heights[index] < stack[-1][0]:
                    while True:
                        if stack:
                            tailNum = stack[-1][0]
                            if tailNum > heights[index]:
                                tailIndex = stack[-1][1]
                                area = tailNum * (index-tailIndex)
                                maxArea = area if area > maxArea else maxArea
                                stack.pop()
                            elif tailNum < heights[index]:
                                stack.append((heights[index],tailIndex))
                                break
                            else: break
                        else:
                            stack.append((heights[index],tailIndex))
                            break
                else: pass
            index += 1
                        
        if stack:
            for s in stack:
                area = s[0] * (index-s[1])
                maxArea = area if area > maxArea else maxArea
        return maxArea
    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        row, col, heights, maxArea = len(matrix), len(matrix[0]), [], 0
        for i in range(row):
            for j in range(col):
                n = int(matrix[i][j])
                if i == 0:
                    heights.append(n)
                else:
                    if not n: heights[j] = 0
                    else: heights[j] += 1
            area = self.largestRectangleArea(heights)
            maxArea = area if area > maxArea else maxArea
        return maxArea