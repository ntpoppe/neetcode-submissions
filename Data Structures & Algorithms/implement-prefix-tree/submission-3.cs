public class PrefixNode 
{
    public PrefixNode[] Children = new PrefixNode[26];
    public bool IsEndOfWord = false;
}

public class PrefixTree {
    public PrefixNode Root;

    public PrefixTree() {
        Root = new PrefixNode();
    }
    
    public void Insert(string word) {
        PrefixNode currNode = this.Root;
        foreach (char ch in word)
        {
            int i = ch - 'a';
            if (currNode.Children[i] == null)
            {
                currNode.Children[i] = new PrefixNode();
            }

            currNode = currNode.Children[i];
        }

        currNode.IsEndOfWord = true;
    }
    
    public bool Search(string word) {
        PrefixNode currNode = this.Root;
        foreach (char ch in word)
        {
            int i = ch - 'a';
            if (currNode.Children[i] == null)
            {
                return false;
            }

            currNode = currNode.Children[i];
        }

        return currNode.IsEndOfWord;
    }
    
    public bool StartsWith(string prefix) {
        PrefixNode currNode = this.Root;
        foreach (char ch in prefix)
        {
            int i = ch - 'a';
            if (currNode.Children[i] == null)
            {
                return false;
            }

            currNode = currNode.Children[i];
        }

        return true;
    }
}
