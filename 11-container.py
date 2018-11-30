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