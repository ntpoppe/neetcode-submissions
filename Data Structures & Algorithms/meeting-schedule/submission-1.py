"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        lastInterval = intervals[0]
        for interval in intervals[1:]:
            if interval.start < lastInterval.end:
                return False
            
            lastInterval = interval

        return True
