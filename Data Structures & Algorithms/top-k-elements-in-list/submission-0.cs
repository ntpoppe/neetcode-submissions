public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var res = new List<int>();
        var freq = new Dictionary<int, int>();
        
        foreach (var num in nums)
        {
            if (!freq.ContainsKey(num))
                freq[num] = 0;

            freq[num]++;
        }

        var buckets = new List<int>[nums.Length + 1];
        foreach (var kvp in freq)
        {
            if (buckets[kvp.Value] == null)
                buckets[kvp.Value] = new List<int>();

            buckets[kvp.Value].Add(kvp.Key);
        }

        for (int i = buckets.Length - 1; i >= 0 && res.Count < k; i--)
        {
            if (buckets[i] != null)
                res.AddRange(buckets[i]);
        }

        return res.ToArray();
    }
}
