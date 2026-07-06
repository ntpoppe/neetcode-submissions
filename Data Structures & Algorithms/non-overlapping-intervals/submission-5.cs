public class Solution {
    public int EraseOverlapIntervals(int[][] intervals) {
        Array.Sort(intervals, (x, y) => x[0].CompareTo(y[0]));

        int result = 0;
        int lastEnd = intervals[0][1];
        foreach (int[] interval in intervals.Skip(1))
        {
            int start = interval[0];
            int end = interval[1];

            if (start < lastEnd)
            {
                result++;
                lastEnd = Math.Min(end, lastEnd);
            }
            else
            {
                lastEnd = end;
            }
        }

        return result;
    }
}
