public class Solution {
    public int Trap(int[] height) {
        var maxLeft = new int[height.Length];
        var maxRight = new int[height.Length];

        // collect max heights from the left
        for (int i = 1; i < height.Length; i++)
        {
            maxLeft[i] = Math.Max(height[i - 1], maxLeft[i -1]);
        }

        // collect max heights from the right
        for (int i = height.Length - 2; i >= 0; i--)
        {
            maxRight[i] = Math.Max(height[i + 1], maxRight[i + 1]);
        }

        // collect rain water
        var waterSum = 0;
        for (int i = 0; i < height.Length; i++)
        {
            var water = Math.Min(maxLeft[i], maxRight[i]) - height[i];
            if (water > 0)
                waterSum += water;
        }

        return waterSum;
    }
}
