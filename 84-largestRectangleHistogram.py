'''
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:
Input: [2,1,5,6,2,3]
Output: 10
'''

class Solution:
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
                                print(area, tailNum, tailIndex, index)
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
        