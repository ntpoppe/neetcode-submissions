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

    # Sort intervals by start time
    # Original overlapping formula: interval1.start < interval2.end && interval2.start < interval2.end
    # After sorting: interval2.start < interval1.end

    # Brute force: For each interval, check existing rooms to see if it overlaps with any
    # present interval. If it doesn't, add it to the room, else create a new room for it.

        rooms: List[List[Interval]] = []
        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            if len(rooms) == 0:
                rooms.append([interval])
                continue

            not_overlapping = False
            for room in rooms:
                if len(room) != 0:
                    if interval.start >= room[-1].end:
                        not_overlapping = True
                        room.append(interval)
                        break 
                        
                if not_overlapping:
                    break

            # Overlap, make new room
            if not not_overlapping:
                rooms.append([interval])

        return len(rooms)

                
 
        