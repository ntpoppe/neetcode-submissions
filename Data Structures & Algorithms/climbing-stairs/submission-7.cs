public class Solution {
    public int ClimbStairs(int n) {
        if (n <= 2)
        {
            return n;
        }

        int[] cache = new int[n];
        for (int i = 0; i < cache.Length; i++)
        {
            cache[i] = 0;
        }

        cache[1] = 1;
        // 1

        cache[2] = 2;
        // 1 + 1
        // 2

        for (int i = 3; i < cache.Length; i++)
        {
            cache[i] = cache[i - 1] + cache[i - 2];
        }

        return cache[n];
    }
}
