public class Solution {
    public int MaxProfit(int[] prices) {
        var left = 0;
        var right = 1;

        var currMax = 0;
        while (right < prices.Length)
        {
            if (prices[left] > prices[right])
            {
                left = right;
                right++;
                continue;
            }

            var profit = prices[right] - prices[left];
            currMax = Math.Max(currMax, profit);
            right++;
        }

        return currMax;
    }
}
