public class Solution {
    public int LargestRectangleArea(int[] heights) {
        var stack = new Stack<int>();
        var maxArea = 0;

        for (int i = 0; i < heights.Length; i++)
        {     
            // keep track of current height      
            // look to the left if possible
                // iterate left until smaller reached
                // keep track of count to left
            // look to the right if possible
                // iterate right until smaller reached
                // keep track of count to right
            // sum counts, multiply by height, if larger than max reassign

            int left = i - 1;
            int leftCount = 0;
            while (left >= 0)
            {
                if (heights[left] >= heights[i])
                {
                    leftCount++;
                    left -= 1;
                    continue;
                }

                break;
            }

            int right = i + 1;
            int rightCount = 0;
            while (right < heights.Length)
            {
                if (heights[right] >= heights[i])
                {
                    rightCount++;
                    right += 1;
                    continue;
                }

                break;
            }

            maxArea = Math.Max(maxArea, (leftCount+rightCount+1) * heights[i]);
        }

        return maxArea;
    }
}
