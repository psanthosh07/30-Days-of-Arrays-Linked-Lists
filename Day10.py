# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        merged=[]
        i=0
        n=len(intervals)
        
        while i<n and intervals[i].end < newInterval.start:
            merged.append(intervals[i])
            i+=1
        while i<n and intervals[i].start<=newInterval.end:
            newInterval.start=min(newInterval.start,intervals[i].start)
            newInterval.end=max(newInterval.end,intervals[i].end)
            i+=1
        merged.append(newInterval)
        
        while i<n:
            merged.append(intervals[i])
            i+=1
        return merged
