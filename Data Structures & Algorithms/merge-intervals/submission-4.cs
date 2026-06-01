public class Solution {
    public int[][] Merge(int[][] intervals) {
        List<int[]> result = new List<int[]>();
        intervals.Sort(x => x[0]);
        foreach (var interval in intervals)
        {
            Console.WriteLine("${interval}");
        }
    }
}
