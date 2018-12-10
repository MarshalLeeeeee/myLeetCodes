'''
56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def getKey(self,interval):
        return interval.start

    def printInterval(self,intervals):
        for i in intervals:
            print(i.start, i.end)
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        length = len(intervals)
        if length == 1: return intervals
        intervals.sort(key=self.getKey)
        left,right,index,ans = intervals[0].start, intervals[0].end,1,[]
        while index < length:
            if right >= intervals[index].start:
                right = max(right,intervals[index].end)
            else:
                ans.append(Interval(left,right))
                left,right = intervals[index].start, intervals[index].end
            index += 1
        ans.append(Interval(left,right))
        return ans

        
if __name__ == '__main__':
	intervals = [Interval(8,10),Interval(15,18),Interval(1,3),Interval(2,6)]
	print(Solution().merge(intervals))