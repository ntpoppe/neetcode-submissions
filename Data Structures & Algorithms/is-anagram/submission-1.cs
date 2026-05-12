public class Solution {
    public bool IsAnagram(string s, string t) {
        var sarr = s.ToCharArray();
        var tarr = t.ToCharArray();
        Array.Sort(sarr);
        Array.Sort(tarr);
        var ss = new string(sarr);
        var st = new string(tarr);

        return new string(sarr) == new string(tarr);
    }
}
