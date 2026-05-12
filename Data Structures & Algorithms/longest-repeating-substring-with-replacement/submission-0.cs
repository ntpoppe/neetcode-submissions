public class Solution {
    public int CharacterReplacement(string s, int k) {
        var freqMap = new Dictionary<char, int>();
        var max = 0;

        int l = 0;
        for (int r = 0; r < s.Length; r++)
        {
            if (!freqMap.ContainsKey(s[r]))
                freqMap[s[r]] = 0;

            freqMap[s[r]]++;

            int maxFreq = int.MinValue; 

            foreach (int value in freqMap.Values)
            {
                if (value > maxFreq)
                    maxFreq = value;
            }

            while ((r - l + 1) - maxFreq > k)
            {
                freqMap[s[l]]--;
                l++;
            }

            max = Math.Max(max, (r - l + 1));
        }

        return max;
    }
}
