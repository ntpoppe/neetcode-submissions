public class Solution {

    public string Encode(IList<string> strs)
    {
        var encoded = string.Empty;

        foreach (var str in strs)
        {
            encoded += str.Length;
            encoded += "/";
            encoded += str;
        }

        return encoded;
    }

    public List<string> Decode(string s)
    {
        if (s == string.Empty) return new List<string>();
        var res = new List<string>();

        // get the length to terminator
        int currPos = 0;
        string numStr = string.Empty;

        while (currPos < s.Length)
        {
            if (s[currPos] == '/')
            {
                var length = int.Parse(numStr);
                res.Add(s.Substring(currPos += 1, length));
                currPos += length;
                numStr = string.Empty;
                continue;
            }

            numStr += s[currPos];
            currPos++;
        }

        return res;
    }
}
