public class Solution {
    public int CharacterReplacement(string s, int k) {
        // provide example cases
        // any constraints?
        // 1 < s.length < 1000
        // 0 < k < s.length
        // no edge cases, always valid
        // only 2 distinct characters in a string

        // how to determine which char to replace?
        // replace least frequent char in window

        var res = 0;
        var freq = new Dictionary<char, int>();
        var l = 0;
        for (int r = 0; r < s.Length; r++)
        {
            if (!freq.ContainsKey(s[r]))
                freq[s[r]] = 0;
            
            freq[s[r]]++;

            var highFreq = 0;
            foreach (int value in freq.Values)
            {
                if (value > highFreq)
                    highFreq = value;
            }

            while((r - l + 1) - highFreq > k)
            {
                freq[s[l]]--;
                l++;
            }

            if ((r - l + 1) > res)
                res = (r - l + 1);
        }

        return res;
    }
}
