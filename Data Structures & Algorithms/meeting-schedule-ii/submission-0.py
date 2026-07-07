"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort the intervals by start time
        # If the first intervals overlaps the second, the first interval should be it's own "room"
        # Continue iterating with the same idea

        if len(intervals) == 0:
            return 0

        res = 1
        lastInterval = intervals[0]
        for interval in intervals[1:]:
            print(f"{interval.start} {lastInterval.end}")
            if interval.start < lastInterval.end:
                res += 1
            
            lastInterval = interval

        return res
        