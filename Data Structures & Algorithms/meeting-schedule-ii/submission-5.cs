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
    public int MinMeetingRooms(List<Interval> intervals) {
        intervals.Sort((x, y) => x.start.CompareTo(y.start));
        List<List<Interval>> rooms = new List<List<Interval>>();

        foreach (Interval interval in intervals)
        {
            if (rooms.Count == 0)
            {
                List<Interval> room = new List<Interval>();
                room.Add(interval);
                rooms.Add(room);
                continue;
            }

            bool overlapping = true;
            foreach (List<Interval> room in rooms)
            {
                if (room.Count != 0 && interval.start >= room[room.Count - 1].end)
                {
                    overlapping = false;
                    room.Add(interval);
                    break;
                }
            }

            if (overlapping)
            {
                rooms.Add(new List<Interval>() { interval });
            }
        }

        return rooms.Count;
    }
}
