class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1. Insert intervals that end before newInterval start into new list
        # 2. Merge any overlapping intervals that exist, if not just insert new interval
        # 3. Append remaining intervals into the newly created list

        ret = []
        while intervals[0][1] < newInterval[0]:
            ret.append(intervals.pop(0))

        i = 0
        # a, b | c, d
        def is_overlap(int1, int2):
            return int1[0] <= int2[1] and int2[0] <= int1[1]

        for interval in intervals:
            if not is_overlap(interval, newInterval):
                print("test")
                ret.append(newInterval)
                return
            else:
                pass

        for interval in intervals:
            ret.append(interval)
        
        print(ret)
        return ret
