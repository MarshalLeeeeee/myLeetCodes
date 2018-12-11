'''
57. Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def binarySearchStart(self,intervals,target):
        left,right = 0,len(intervals)-1
        while left <= right:
            mid = (left+right) // 2
            if intervals[mid].start < target:
                left = mid + 1
            elif intervals[mid].start > target:
                right = mid - 1
            else:
                return mid
        return right
    
    def binarySearchEnd(self, intervals, target):
        left,right = 0,len(intervals)-1
        while left <= right:
            mid = (left+right) // 2
            if intervals[mid].end < target:
                left = mid + 1
            elif intervals[mid].end > target:
                right = mid - 1
            else:
                return mid
        return left
    
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals: return [newInterval]
        leftMost = self.binarySearchStart(intervals,newInterval.start)
        rightMost = self.binarySearchEnd(intervals,newInterval.end)
        if leftMost == -1: 
            newStart,left = newInterval.start,0
        else: 
            if intervals[leftMost].end >= newInterval.start:
                newStart,left = intervals[leftMost].start,leftMost
            else:
                newStart,left = newInterval.start, leftMost+1
                
        if rightMost == len(intervals):
            newEnd,right = newInterval.end, len(intervals)
        else:
            if intervals[rightMost].start <= newInterval.end:
                newEnd,right = intervals[rightMost].end,rightMost+1
            else:
                newEnd,right = newInterval.end,rightMost
        return intervals[:left]+[Interval(newStart,newEnd)]+intervals[right:]