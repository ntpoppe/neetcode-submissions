public class Solution {
    Dictionary<int, List<int>> AdjList = new();
    HashSet<int> Visited = new();

    public bool ValidTree(int n, int[][] edges)
    { 
        for (int i = 0; i < n; i++)
        {
            AdjList[i] = new List<int>();
        }

        foreach (int[] edge in edges)
        {
            AdjList[edge[0]].Add(edge[1]);
            AdjList[edge[1]].Add(edge[0]);
        }

        if (!Dfs(0, -1))
        {
            return false;
        }

        return Visited.Count == n;
    }

    public bool Dfs(int node, int parent)
    {
        if (Visited.Contains(node))
        {
            return false;
        }

        Visited.Add(node);

        foreach (int neighbor in AdjList[node])
        {
            if (neighbor != parent)
            {
                if (!Dfs(neighbor, node))
                { 
                    return false;
                }
            }
        }

        return true;
    }
}
