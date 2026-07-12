public class Solution {
    public int ClimbStairs(int n) {     
        return Dfs(0, n);
    }

    public int Dfs(int i, int n)
    {
        if (i >= n)
        {
            return i == n ? 1 : 0;
        }

        return Dfs(i + 1, n) + Dfs(i + 2, n);
    }
}
