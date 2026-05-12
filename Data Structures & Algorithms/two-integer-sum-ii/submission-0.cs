public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        var res = new int[2];

        int i = 0;
        int j = numbers.Length - 1;

        while (i < j)
        {
            var sum = numbers[i] + numbers[j];
            if (sum < target)
            {
                i++;
                continue;
            }

            if (sum > target)
            {
                j--;
                continue;
            }

            if (sum == target)
            {
                return new int[2] { i + 1, j + 1 };
            }
        }

        return new int[2] { -1, -1 };
    }
}
