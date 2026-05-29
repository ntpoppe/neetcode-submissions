public class Solution {
    public List<char> Result = new List<char>();
    public Dictionary<char, bool> Visited = new Dictionary<char, bool>();
    public Dictionary<char, HashSet<char>> AdjList = new Dictionary<char, HashSet<char>>();

    public string foreignDictionary(string[] words) {
        List<List<char>> edges = new List<List<char>>();

        foreach (string word in words)
        {
            foreach (char ch in word)
            {
                AdjList[ch] = new HashSet<char>();
            }
        }

        for (int i = 0; i < words.Length - 1; i++)
        {
            string word1 = words[i];
            string word2 = words[i + 1];
            
            if (word1.Length > word2.Length && word1.Contains(word2))
            {
                return string.Empty;
            }

            int letter_pointer = 0;
            while (letter_pointer < word1.Length && letter_pointer < word2.Length)
            {
                if (word1[letter_pointer] != word2[letter_pointer])
                {
                    edges.Add(new List<char>() { word1[letter_pointer], word2[letter_pointer]});
                }
                letter_pointer++;
            }
        }

        foreach (var edge in edges)
        {
            AdjList[edge[0]].Add(edge[1]);
        }

        foreach (char key in AdjList.Keys)
        {
            if (Dfs(key))
            {
                return "";
            }
        }

        Result.Reverse();
        return string.Join("", Result);
    }

    public bool Dfs(char letter)
    {
        if (Visited.ContainsKey(letter))
        {
            return Visited[letter];
        }

        Visited[letter] = true;

        foreach (char neighbor in AdjList[letter])
        {
            if (Dfs(neighbor))
            {
                return true;
            }
        }

        Visited[letter] = false;
        Result.Add(letter);
        return false;
    }
}
