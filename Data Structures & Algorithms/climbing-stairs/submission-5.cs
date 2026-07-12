public class Solution {
    public int[] Cache = new int[50];

    public int ClimbStairs(int n) {    
        for (int i = 0; i < Cache.Length; i++)
        {
            Cache[i] = -1;
        } 

        return Dfs(0, n);
    }

    public int Dfs(int i, int n)
    {
        if (i >= n)
        {
            return i == n ? 1 : 0;
        }

        if (Cache[i] != -1)
        {
            return Cache[i];
        }

        Cache[i] = Dfs(i + 1, n) + Dfs(i + 2, n);
        return Cache[i]; 
    }
}
