/**
 * Definition of Interval:
 * public class Interval {
 *     public int start, end;
 *     public Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 * }
 */

public class Solution {
    public bool CanAttendMeetings(List<Interval> intervals) {
        if (intervals.Count == 0)
        {
            return true;
        }

        List<Interval> sorted = intervals.OrderBy(i => i.start).ToList();

        Interval lastInterval = sorted.First();
        foreach (Interval interval in sorted.Skip(1))
        {
            if (interval.start < lastInterval.end)
            {
                return false;
            }

            lastInterval = interval;
        }

        return true;
    }
}   
