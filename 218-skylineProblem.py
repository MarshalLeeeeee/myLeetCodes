'''
218. The Skyline Problem

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), 
write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. 
It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 
A key point is the left endpoint of a horizontal line segment. 
Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. 
Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:
The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. 
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''

class Solution: 
    def judge(self,left,right):
        if left[0] < right[0]: return 1
        elif left[0] > right[0]: return 0
        else: return 1 if left[1] > right[1] else 0
    
    def append(self,pos,res):
        if res and pos[0] == res[-1][0] and pos[1] <= res[-1][1]: return
        else: res.append(pos)
        
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings: return []
        elif len(buildings) == 1: return [[buildings[0][0],buildings[0][2]],[buildings[0][1],0]]
        else:
            length = len(buildings)
            left = self.getSkyline(buildings[:length//2])
            right = self.getSkyline(buildings[length//2:])
            res,lh,lx,li,rh,rx,ri = [],-1,-1,0,-1,-1,0
            prevFlag = None
            while li < len(left) and ri < len(right):
                flag = 1 if self.judge(left[li],right[ri]) else 0
                if flag:
                    if prevFlag == None or prevFlag == flag or left[li][1] != rh:
                        if left[li][0] < rx:
                            if left[li][1] > rh: self.append(left[li],res)
                            elif rh > left[li][1] and lh > rh: self.append([left[li][0],rh],res)
                        else: self.append(left[li],res)
                    lh,lx = left[li][1],left[li+1][0] if li+1<len(left) else -1
                    li += 1
                else:
                    if prevFlag == None or prevFlag == flag or right[ri][1] != lh:
                        if right[ri][0] < lx:
                            if right[ri][1] > lh: self.append(right[ri],res)
                            elif lh > right[ri][1] and rh > lh: self.append([right[ri][0],lh],res)
                        else: self.append(right[ri],res)
                    rh,rx = right[ri][1],right[ri+1][0] if ri+1<len(right) else -1
                    ri += 1
                prevFlag = flag
            if li == len(left): 
                self.append(right[ri],res)
                return res+right[ri+1:]
            else: 
                self.append(left[li],res)
                return res+left[li+1:]

if __name__ == '__main__':
    #print(Solution().getSkyline([[0,5,7],[5,10,7],[5,10,12],[10,15,7],[15,20,7],[15,20,12],[20,25,7]]))
    # [[0,7],[5,12],[10,7],[15,12],[20,7],[25,0]]
    print(Solution().getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    # [[0,7],[5,12],[10,7],[15,12],[20,7],[25,0]]