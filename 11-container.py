'''
11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container and n is at least 2.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    # fail when the input is squencial
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def getKey(h):
            return h[0]
        
        def findMin(h):
            minIndex = h[0][1]
            for i in range(1,len(h)):
                m = h[i][1]
                minIndex = m if m < minIndex else minIndex
            return minIndex
        
        def findMax(h):
            maxIndex = h[0][1]
            for i in range(1,len(h)):
                m = h[i][1]
                maxIndex = m if m > maxIndex else maxIndex
            return maxIndex
        
        heightIndex = [(h,i) for i,h in enumerate(height)]
        heightIndex.sort(key=getKey)
        
        heightLen = len(heightIndex)
        maxIndex = heightLen - 1
        minIndex = 0
        maxV = 0
        for i in range(heightLen-1):
            v = heightIndex[i][0] * max(maxIndex-heightIndex[i][1],heightIndex[i][1]-minIndex)
            if v > maxV:
                maxV = v
            if heightIndex[i][1] == minIndex:
                minIndex = findMin(heightIndex[i+1:])
            if heightIndex[i][1] == maxIndex:
                maxIndex = findMax(heightIndex[i+1:]) 
        return maxV


class Solution2:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """        
        heightLen = len(height)
        if(heightLen < 2):
            return 0
        left = 0
        right = heightLen-1
        maxV = 0
        while left < right:
            gap = right-left
            if(height[left]<height[right]):
                v = height[left] * gap
                left += 1
            else:
                v = height[right] * gap
                right -= 1
            maxV = v if v>maxV else maxV
        return maxV