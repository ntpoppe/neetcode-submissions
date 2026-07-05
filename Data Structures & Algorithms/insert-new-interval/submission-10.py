class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        # 1. Insert intervals that end before newInterval start into new list
        # 2. Merge any overlapping intervals that exist, if not just insert new interval
        # 3. Append remaining intervals into the newly created list

        ret = []
        print(f"{intervals[0][1]=}")
        while intervals[0][1] < newInterval[0]:
            ret.append(intervals.pop(0))

        print(f"after first: {ret=}")

        def is_overlap(int1, int2):
            return int1[0] <= int2[1] and int2[0] <= int1[1]

        merged_int = newInterval
        while len(intervals) > 0 and is_overlap(intervals[0], newInterval):
            print(f"{intervals[0]=} {newInterval=}")
            new_min = min(intervals[0][0], merged_int[0])
            new_max = max(intervals[0][1], merged_int[1])
            merged_int = [new_min, new_max]
            intervals.pop(0)

        ret.append(merged_int)
                
        for interval in intervals:
            ret.append(interval)
        
        print(ret)
        return ret
