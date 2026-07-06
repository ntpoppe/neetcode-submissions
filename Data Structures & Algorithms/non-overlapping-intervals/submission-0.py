class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def is_overlapping(i1, i2):
            return i1[0] < i2[1] and i2[0] < i1[1]

        intervals.sort(key=lambda x: x[0])
        print(f"pre {intervals=}")

        i = 0
        res = 0
        while i < len(intervals) - 1:
            print(f"iter {i=} {intervals=}")
            if is_overlapping(intervals[i], intervals[i + 1]):
                intervals.pop(i + 1)
                res += 1
            else:
                i += 1

        return res