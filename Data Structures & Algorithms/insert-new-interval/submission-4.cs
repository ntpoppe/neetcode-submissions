public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) 
    {
        List<int[]> output = new List<int[]>();

        int i = 0;
        int n = intervals.Length;
        while (i < n && intervals[i][1] <= newInterval[0])
        {
            output.Add(intervals[i]);
            i++;
        }

        while (i < n && intervals[i][0] <= newInterval[1])
        {
            newInterval[0] = Math.Min(intervals[i][0], newInterval[0]);
            newInterval[1] = Math.Max(intervals[i][1], newInterval[1]);
            i++;
        }

        output.Add(newInterval);

        while (i < n)
        {
            output.Add(intervals[i]);
            i++;
        }


        return output.ToArray();
    }
}
