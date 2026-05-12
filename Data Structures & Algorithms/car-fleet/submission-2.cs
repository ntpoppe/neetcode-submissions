public class Solution {
    public int CarFleet(int target, int[] position, int[] speed) {
var res = 0;
        var combinedArr = new (int pos, int spd)[position.Length];

        for (int i = 0; i < position.Length; i++)
        {
            combinedArr[i] = (position[i], speed[i]);
        }

        combinedArr = combinedArr.OrderByDescending(e => e.pos).ToArray();

        var stack = new Stack<(int pos, int spd)>();
        foreach (var (pos, spd) in combinedArr)
        {
            if (stack.Count == 0)
            {
                stack.Push((pos, spd));
                continue;
            }

            var curTime = (double)(target - pos) / spd;
            var (stackPos, stackSpd) = stack.Peek();
            var stackTime = (double)(target - stackPos) / stackSpd;
            if (curTime > stackTime)
                stack.Push((pos, spd));
        }

        return stack.Count;
    }
}
