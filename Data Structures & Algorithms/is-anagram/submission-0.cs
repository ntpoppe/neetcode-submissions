public class Solution {
    public bool IsAnagram(string s, string t) {
        var hashMap = new Dictionary<char, int>();

        foreach (var ch in s)
        {
            if (!hashMap.ContainsKey(ch))
                hashMap[ch] = 0;

            hashMap[ch]++;
        }

        foreach (var ch in t)
        {
            if (!hashMap.ContainsKey(ch))
                hashMap[ch] = 0;

            hashMap[ch]--;
        }

        return !hashMap.Values.Where(v => v != 0).Any();
    }
}
