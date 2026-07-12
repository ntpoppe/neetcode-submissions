public class Solution {
    public bool CanJump(int[] nums) {
        if (nums.Length == 1)
        {
            return true;
        }

        int n = nums.Length;
        int goal = n - 1;
        int current = n - 2;
        bool fullReach = false;

        while (current >= 0)
        {
            if (current + nums[current] >= goal)
            {
                if (current == 0)
                {
                    fullReach = true;
                    break;
                }

                goal = current;
                current--;
            }
            else
            {
                current--;
            }
        }

        return fullReach;
    }
}
