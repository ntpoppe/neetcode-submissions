public class Solution {
    public Dictionary<int, List<int>> PrereqMap = new();
    public HashSet<int> Visited = new();

    public bool CanFinish(int numCourses, int[][] prerequisites) 
    {
        for (int i = 0; i < numCourses; i++)
        {
            PrereqMap[i] = new List<int>();
        }

        foreach (int[] prereq in prerequisites)
        {
            PrereqMap[prereq[0]].Add(prereq[1]);
        }

        for (int i = 0; i < numCourses; i++)
        {
            if (Dfs(i) == false)
            {
                return false;
            }
        }

        return true;
    }

    public bool Dfs(int courseID)
    {
        if (Visited.Contains(courseID))
        {
            return false;
        }

        if (PrereqMap[courseID].Count == 0)
        {
            return true;
        }

        Visited.Add(courseID);
        foreach (int prereq in PrereqMap[courseID])
        {
            if (Dfs(prereq) == false)
            {
                return false;
            }
        }
        Visited.Remove(courseID);
        PrereqMap[courseID] = new List<int>();

        return true;
    }
}
