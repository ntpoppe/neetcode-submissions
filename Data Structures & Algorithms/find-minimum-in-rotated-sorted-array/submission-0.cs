public class Solution {
    public int FindMin(int[] nums) {
        var res = nums[0];

        var l = 0;
        var r = nums.Length - 1;

        while (l <= r)
        {
            if (nums[l] < nums[r])
            {
                res = Math.Min(res, nums[l]);
                break;
            }

            int mid = (l + r) / 2;
            res = Math.Min(res, nums[mid]);

            if (nums[mid] >= nums[l])
                l = mid + 1;
            else
                r = mid - 1;
        }

        return res;
    }
}
