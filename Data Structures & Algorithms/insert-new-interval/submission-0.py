class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if interval[1] < newInterval[0]:
                output.append(intervals.pop(i))
            else:
                i += 1

        i = 0
        merged_interval = newInterval
        while i < len(intervals):
            if self.isOverlapping(merged_interval, intervals[i]):
                print(i)
                interval = intervals[i]
                min_start = min(merged_interval[0], interval[0])
                max_end = max(merged_interval[1], interval[1])
                merged_interval = [min_start, max_end]
                intervals.pop(i)
            else:
                i += 1
        output.append(merged_interval)

        for interval in intervals:
            output.append(interval)

        return output

    def isOverlapping(self, newInterval: List[int], existingInterval: List[int]):
        print(f"isOverlapping {newInterval=} {existingInterval=}")
        # New start could be less than existing start, but new end could be less then existing end but greater than existing start
        # New start could be greater than existing start but less than existing end, but new end could be greater than existing end
        # New interval could swallow existing interval
        # Existing interval could swallow new interval 

        if newInterval[0] <= existingInterval[0] and newInterval[1] <= existingInterval[1] and newInterval[1] >= existingInterval[0]:
            print("overlapping by start less than case")
            return True

        if newInterval[0] >= existingInterval[0] and newInterval[0] <= existingInterval[1] and newInterval[1] >= existingInterval[1]:
            print("overlapping by start greater than case")
            return True
        
        if newInterval[0] <= existingInterval[0] and newInterval[1] >= existingInterval[1]:
            print("overlapping by newInterval swallowing existing case")
            return True

        if newInterval[0] >= existingInterval[0] and newInterval[1] <= existingInterval[1]:
            print("overlapping by existingInterval swallowing new case")
            return True

        print("not overlapping")
        return False

