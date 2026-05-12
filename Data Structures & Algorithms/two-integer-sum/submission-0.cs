public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        
        // subtract target from i. val is key index if val
        var map = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            var compliment = target - nums[i];
            if (map.ContainsKey(compliment))
                return new int[2] {map[compliment], i};
            map[nums[i]] = i;
        }

        return new int[] { -1, -1 };
    }
}
