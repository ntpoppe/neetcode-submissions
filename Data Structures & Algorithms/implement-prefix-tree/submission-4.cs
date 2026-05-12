public class TrieNode {
    public TrieNode[] Children = new TrieNode[26];
    public bool IsWord = false;
}

public class PrefixTree {

    TrieNode Root { get; set; }

    public PrefixTree() {
        Root = new TrieNode();
    }
    
    public void Insert(string word) {
        TrieNode curr = Root;
        for (int i = 0; i < word.Length; i++)
        {
            int childIndex = word[i] - 'a';
            if (curr.Children[childIndex] == null)
            {
                curr.Children[childIndex] = new TrieNode();
            }

            if (i == word.Length - 1)
            {
                curr.Children[childIndex].IsWord = true;
            }

            curr = curr.Children[childIndex];
        }
    }
    
    public bool Search(string word) {
        TrieNode curr = Root;
        for (int i = 0; i < word.Length; i++)
        {
            int childIndex = word[i] - 'a'; 
            if (curr.Children[childIndex] == null)
            {
                return false;
            }

            curr = curr.Children[childIndex];
        }

        return curr.IsWord;
    }
    
    public bool StartsWith(string prefix) {
        TrieNode curr = Root;
        for (int i = 0; i < prefix.Length; i++)
        {
            int childIndex = prefix[i] - 'a'; 
            if (curr.Children[childIndex] == null)
            {
                return false;
            }

            curr = curr.Children[childIndex];
        }

        return true;
    }
}
