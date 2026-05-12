public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var res = new List<List<string>>();
        var map = new Dictionary<string, List<string>>();

        foreach (var str in strs)
        {
            var strArr = str.ToCharArray();
            Array.Sort(strArr);
            var sortedStr = new string(strArr);

            if (!map.ContainsKey(sortedStr))
                map[sortedStr] = new List<string>();

            map[sortedStr].Add(str);
        }

        foreach (var kvp in map)
        {
            res.Add(kvp.Value);
        }

        return res;
    }
}
