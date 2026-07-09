"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # (0, 2), (2, 4), (3, 5), (5, 6), (5, 7)
        # Room 1: (0, 2), (2, 4), (5, 6)
        # Room 2: (3, 5), (5, 7)

        # A better solution: a heap.
        # We can use a heap to keep track of the end times of meetings. The earliest end time
        # will always be at the top of the heap. If an interval overlaps, we can push to the heap.
        # If it doesnt overlap with the top of the heap, we can pop that and then push.

        intervals.sort(key=lambda i: i.start)
        heap = []

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)

        return len(heap) 



                
 
        