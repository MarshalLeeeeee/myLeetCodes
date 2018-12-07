'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def findAcsendingTop(self,height):
        length = len(height)
        if length == 1:
            return [0]
        ascend = []
        i, lastAcsend, maxHeight = 1, 0, height[0]
        flag = True
        while(i < length):
            if height[i] > height[i-1] and height[i] > maxHeight:
                flag = True
                lastAcsend = i
                maxHeight = height[i]
            elif height[i] < height[i-1]:
                if flag:
                    ascend.append(lastAcsend)
                    flag = False
            else:
                pass
            i += 1
        if flag: ascend.append(lastAcsend)
        return ascend

    def getConnect(self,height,headAcsend,tailAcsend,top):
        connect = 0
        index = headAcsend[0]
        headI, tailI = 1, 0
        while(headI < len(headAcsend)):
            connect += top - max(height[index],height[headAcsend[headI]])
            if index == headAcsend[headI]:
                headI += 1
            index += 1
        while(index<tailAcsend[0]):
            if top > height[index]:
                connect += top - height[index]
            index += 1
        while(index<=tailAcsend[-1]):
            if top > height[tailAcsend[tailI]]:
                connect += top - min(max(height[index],height[tailAcsend[tailI]]),top)
                index += 1
                if tailI < len(tailAcsend) - 1 and index == tailAcsend[tailI+1]:
                    tailI += 1
            else:
                return connect
        #return connect
    
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        if length < 3:
            return 0
        head = height[:length//2]
        tail = height[length//2:]
        headWater = self.trap(head)
        tailWater = self.trap(tail)

        headAcsend = self.findAcsendingTop(head[::-1])
        tailAcsend = self.findAcsendingTop(tail)
        headAcsend = [len(head)-1-x for x in headAcsend]
        headAcsend = headAcsend[::-1]
        tailAcsend = [x+length//2 for x in tailAcsend]
        acsend = headAcsend + tailAcsend
        
        headTop = height[acsend[0]]
        tailTop = height[acsend[-1]]
        connect = 0
        if headTop < tailTop:
            connect = self.getConnect(height,headAcsend,tailAcsend,headTop)
        else:
            height = height[::-1]
            headAcsend = [len(tail)+(len(head)-1-x) for x in headAcsend]
            tailAcsend = [len(tail)-1-(x-length//2) for x in tailAcsend]
            connect = self.getConnect(height,tailAcsend[::-1],headAcsend[::-1],tailTop)   
        return headWater+tailWater+connect

if __name__ == '__main__':
    maps = [5,0,3,0,4,0,2,1,1,3,0,4,0,2,0,2,0,7,0]
    maps2 = [5,4,1,2]
    maps3 = [5,2,1,2,1,5]
    maps4 = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
    print(Solution().trap(maps4))