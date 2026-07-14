public class Solution {
    int[] Cache = new int[50];
    
    public int Rob(int[] nums) {
        for (int i = 0; i < Cache.Length; i++)
        {
            Cache[i] = -1;
        }

        return Dfs(0, nums);
    }

    public int Dfs(int i, int[] nums)
    {
        if (i == nums.Length - 1)
        {
            return nums[i];
        }
        else if (i >= nums.Length)
        {
            return 0;
        }

        if (Cache[i] != -1)
        {
            return Cache[i];
        }

        Cache[i] = Math.Max(nums[i] + Dfs(i + 2, nums), Dfs(i + 1, nums));
        return Cache[i];
    }
}
