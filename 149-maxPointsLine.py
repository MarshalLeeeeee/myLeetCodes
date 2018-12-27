'''
149. Max Points on a Line

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
'''

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # O(n^2) time
    def gcd(self,a,b):
        if a < b: a,b = b, a
        while b:
            a,b = b, a%b
        return a
    
    def reduction(self, a, b):
        if not a: return 1,0
        elif not b: return 0,1
        else:
            gcd = self.gcd(abs(a),abs(b))
            a, b = a // gcd, b // gcd
            a, b = b, -a
            if a < 0: return -a, -b
            else: return a, b
    
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length = len(points)
        if not length: return 0
        elif length == 1: return 1
        else:
            pointDic, dic, res = {}, {}, 0
            for i in range(length):
                '''
                try: pointDic[(points[i].x,points[i].y)] += 1
                except: pointDic[(points[i].x,points[i].y)] = 1
                '''
                try: pointDic[points[i]] += 1
                except: pointDic[points[i]] = 1
                for j in range(i+1, length):
                    xDelta,yDelta = points[j].x-points[i].x, points[j].y-points[i].y
                    a,b = self.reduction(xDelta,yDelta)
                    c = a * points[i].x + b * points[i].y
                    if (a,b,c) in dic: 
                        if points[i] not in dic[(a,b,c)][1]: dic[(a,b,c)][0] += 1; dic[(a,b,c)][1] |= set([points[i]])
                        if points[j] not in dic[(a,b,c)][1]: dic[(a,b,c)][0] += 1; dic[(a,b,c)][1] |= set([points[j]])
                    else: dic[(a,b,c)] = [2,set([points[i],points[j]])]
                    if dic[(a,b,c)][0] > res: res = dic[(a,b,c)][0]
            return res