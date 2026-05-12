public class TrieNode 
{
    public Dictionary<char, TrieNode> Children = new();
    public bool IsWord = false;

    public void AddWord(string word)
    {
        TrieNode current = this;

        foreach (char letter in word)
        {
            if (!current.Children.TryGetValue(letter, out TrieNode node))
            {
                node = new TrieNode();
                current.Children[letter] = node;
            }

            current = node;
        }

        current.IsWord = true;
    }
}

public class Solution 
{
    public List<string> FindWords(char[][] board, string[] words) 
    {
        TrieNode root = new TrieNode();
        foreach (string word in words)
        {
            root.AddWord(word);
        }

        HashSet<string> result = new();
        HashSet<(int, int)> path = new();

        for (int r = 0; r < board.Length; r++)
        {
            for (int c = 0; c < board[0].Length; c++)
            {
                Dfs(r, c, root, "", path, board, words, result);
            } 
        }

        return result.ToList();
    }

    public void Dfs(int r, int c, TrieNode node, string word, HashSet<(int, int)> path, char[][] board, string[] words, HashSet<string> result)
    {
        if (r < 0 || r >= board.Length || c < 0 || c >= board[0].Length ||
            path.Contains((r, c)) || !node.Children.ContainsKey(board[r][c]))
        {
            return;
        }

        char letter = board[r][c];
        word = word + letter;
        node = node.Children[letter];

        if (node.IsWord && words.Contains(word))
        {
            result.Add(word);
        }

        path.Add((r, c));

        Dfs(r + 1, c, node, word, path, board, words, result);
        Dfs(r - 1, c, node, word, path, board, words, result);
        Dfs(r, c + 1, node, word, path, board, words, result);
        Dfs(r, c - 1, node, word, path, board, words, result);

        path.Remove((r, c));
    }
}
