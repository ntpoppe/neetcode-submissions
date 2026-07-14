public class Solution {
    public int Rob(int[] nums) {
        int[] cache = new int[nums.Length];
        for (int i = 0; i < cache.Length; i++)
        {
            cache[i] = -1;
        }

        return Dfs(0, nums, cache);
    }

    public int Dfs(int i, int[] nums, int[] cache)
    {
        if (i == nums.Length - 1)
        {
            return nums[i];
        }
        else if (i >= nums.Length)
        {
            return 0;
        }

        if (cache[i] != -1)
        {
            return cache[i];
        }

        cache[i] = Math.Max(nums[i] + Dfs(i + 2, nums, cache), Dfs(i + 1, nums, cache));
        return cache[i];
    }
}
