class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Overlaps if:
        # Start/end point of one interval is the start/end point of another
        # One interval swallows another

        # Are the intervals in "intervals" always sorted?

        # Loop through "intervals". If overlapping criteria is met, take min start and max end of each.
        # Add to resulting list.

        def is_overlapping(interval1: List[int], interval2: List[int]) -> bool:
            return interval1[0] <= interval2[1] and interval2[0] <= interval1[1]

        res = [intervals[0]]
        res_last_index = 0
        i = 1
        while i < len(intervals):
            if is_overlapping(res[res_last_index], intervals[i]):
                min_start = min(res[res_last_index][0], intervals[i][0])
                max_end = max(res[res_last_index][1], intervals[i][1])
                res[res_last_index][0] = min_start
                res[res_last_index][1] = max_end
            else:
                res.append(intervals[i])
                res_last_index += 1
            i += 1

        return res