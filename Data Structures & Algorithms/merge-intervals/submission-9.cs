public class Solution {
    public int[][] Merge(int[][] intervals) {
        Array.Sort(intervals, (x, y) => x[0].CompareTo(y[0]));

        List<int[]> res = new List<int[]>();
        res.Add(intervals[0]);

        foreach (int[] interval in intervals)
        {
            int lastEnd = res[res.Count - 1][1];
            if (interval[0] <= lastEnd)
            {
                res[res.Count - 1][1] = Math.Max(lastEnd, interval[1]);
            }
            else
            {
                res.Add(interval);
            }
        }

        return res.ToArray();
    }
}
