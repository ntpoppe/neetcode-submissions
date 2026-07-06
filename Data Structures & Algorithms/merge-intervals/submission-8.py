class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        def is_overlapping(i1, i2):
            return i1[0] <= i2[1] and i2[0] <= i1[1]

        res = []

        ptr = intervals.pop(0)
        while len(intervals) > 0:
            if not is_overlapping(ptr, intervals[0]):
                popped = intervals.pop(0)
                res.append(ptr)
                ptr = popped
            else:
                popped = intervals.pop(0)
                new_min = min(ptr[0], popped[0])
                new_max = max(ptr[1], popped[1])
                ptr = [new_min, new_max]
        
        res.append(ptr)

        return res

